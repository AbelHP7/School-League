from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# 1. Custom User Model with Roles
class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('TEACHER', 'Profesor'),
        ('STUDENT', 'Alumno'),
        ('REFEREE', 'Árbitro'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='STUDENT')

    def save(self, *args, **kwargs):
        if self.role == 'ADMIN':
            self.is_staff = True
            self.is_superuser = True
        else:
            self.is_staff = False
            self.is_superuser = False
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

# 2. Team Model
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Equipo")
    coach = models.CharField(max_length=100, verbose_name="Entrenador/Tutor")
    shield = models.ImageField(upload_to='shields/', blank=True, null=True, verbose_name="Escudo")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# 3. Player Model
class Player(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    dorsal = models.PositiveIntegerField(verbose_name="Dorsal")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players', verbose_name="Equipo")

    class Meta:
        unique_together = ('team', 'dorsal')

    def __str__(self):
        return f"{self.name} (#{self.dorsal}) - {self.team.name}"

# 4. Match Model
class Match(models.Model):
    STATUS_CHOICES = (
        ('SCHEDULED', 'Programado'),
        ('PLAYING', 'En Juego'),
        ('FINISHED', 'Finalizado'),
        ('SUSPENDED', 'Suspendido'),
    )

    PHASE_CHOICES = (
        ('LEAGUE', 'Fase Liga'),
        ('PLAYOFF', 'Play-Off'),
        ('QUARTERS', 'Cuartos de Final'),
        ('SEMIS', 'Semifinal'),
        ('FINAL', 'Final'),
    )

    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches', verbose_name="Equipo Local")
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches', verbose_name="Equipo Visitante")
    match_date = models.DateTimeField(verbose_name="Fecha y Hora")
    location = models.CharField(max_length=100, default="Pista Central", verbose_name="Lugar")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='SCHEDULED', verbose_name="Estado")
    phase = models.CharField(max_length=20, choices=PHASE_CHOICES, default='LEAGUE', verbose_name="Fase")
    
    home_score = models.PositiveIntegerField(default=0, verbose_name="Goles Local")
    away_score = models.PositiveIntegerField(default=0, verbose_name="Goles Visitante")
    
    round = models.PositiveIntegerField(default=1, verbose_name="Jornada")

    referee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'role': 'REFEREE'}, verbose_name="Árbitro")

    class Meta:
        verbose_name_plural = "Matches"

    def __str__(self):
        return f"[{self.get_phase_display()}] {self.home_team} vs {self.away_team} ({self.match_date.strftime('%d/%m %H:%M')})"

class KnockoutTie(models.Model):
    """
    Groups two matches (first leg and second leg) or a single match into a knockout tie.
    Evaluates who advances to the next round.
    """
    phase = models.CharField(max_length=20, choices=Match.PHASE_CHOICES, verbose_name="Fase Eliminatoria")
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='ties_as_team1')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='ties_as_team2')
    
    match_1_id = models.ForeignKey(Match, null=True, blank=True, on_delete=models.SET_NULL, related_name='tie_leg_1')
    match_2_id = models.ForeignKey(Match, null=True, blank=True, on_delete=models.SET_NULL, related_name='tie_leg_2')

    winner = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL, related_name='won_ties')

    def __str__(self):
        return f"{self.get_phase_display()}: {self.team1} vs {self.team2}"

# 5. Goal Model
class Goal(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='goals', verbose_name="Partido")
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='goals', verbose_name="Jugador")
    minute = models.PositiveIntegerField(verbose_name="Minuto")

    def __str__(self):
        return f"Gol de {self.player} ({self.minute}')"

# 6. Standing (Clasificación) Model
class Standing(models.Model):
    team = models.OneToOneField(Team, on_delete=models.CASCADE, related_name='standing', verbose_name="Equipo")
    played = models.PositiveIntegerField(default=0)
    won = models.PositiveIntegerField(default=0)
    drawn = models.PositiveIntegerField(default=0)
    lost = models.PositiveIntegerField(default=0)
    goals_for = models.PositiveIntegerField(default=0)
    goals_against = models.PositiveIntegerField(default=0)
    points = models.PositiveIntegerField(default=0)

    @property
    def goal_difference(self):
        return self.goals_for - self.goals_against

    def __str__(self):
        return f"{self.team.name}: {self.points} pts"

    class Meta:
        ordering = ['-points', '-goals_for'] # Simple ordering, complex ones can be done in views

# Signals to Auto-Create Standing when Team is created
@receiver(post_save, sender=Team)
def create_team_standing(sender, instance, created, **kwargs):
    if created:
        Standing.objects.create(team=instance)

# Logic to update standings
@receiver(post_save, sender=Match)
def update_standings(sender, instance, **kwargs):
    # Ensure standings are only updated for League phase matches
    if instance.status == 'FINISHED' and instance.phase == 'LEAGUE':
        recalculate_standing(instance.home_team)
        recalculate_standing(instance.away_team)

def recalculate_standing(team):
    standing, _ = Standing.objects.get_or_create(team=team)
    
    # Get all finished LEAGUE matches for this team
    home_matches = Match.objects.filter(home_team=team, status='FINISHED', phase='LEAGUE')
    away_matches = Match.objects.filter(away_team=team, status='FINISHED', phase='LEAGUE')
    
    played = home_matches.count() + away_matches.count()
    won = 0
    drawn = 0
    lost = 0
    goals_for = 0
    goals_against = 0
    
    # Process Home Matches
    for m in home_matches:
        goals_for += m.home_score
        goals_against += m.away_score
        if m.home_score > m.away_score:
            won += 1
        elif m.home_score == m.away_score:
            drawn += 1
        else:
            lost += 1
            
    # Process Away Matches
    for m in away_matches:
        goals_for += m.away_score
        goals_against += m.home_score
        if m.away_score > m.home_score:
            won += 1
        elif m.away_score == m.home_score:
            drawn += 1
        else:
            lost += 1
            
    # Update Standing
    standing.played = played
    standing.won = won
    standing.drawn = drawn
    standing.lost = lost
    standing.goals_for = goals_for
    standing.goals_against = goals_against
    standing.points = (won * 3) + (drawn * 1)
    standing.save()
