from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.contrib.auth import login
from .models import Match, Standing, Team
from .forms import StudentRegistrationForm
from .generator import generate_league_phase_matches

def signup(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Auto-login after registration
            messages.success(request, "¡Registro completado! Bienvenido.")
            return redirect('index')
    else:
        form = StudentRegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})

def index(request):
    return render(request, 'tournament/index.html')

@staff_member_required
def generate_matches(request):
    count, message = generate_league_phase_matches()

    if count > 0:
        messages.success(request, message)
    else:
        messages.warning(request, message)
    return redirect('matches')

@login_required
def profile(request):
    return render(request, 'tournament/profile.html')

def standings(request):
    # Standings are ordered by points (desc), then goals_for (desc)
    table = Standing.objects.select_related('team').order_by('-points', '-goals_for')
    num_teams = table.count()
    
    direct_limit = 0
    playoff_limit = 0
    
    if num_teams > 0:
        direct_limit = max(1, num_teams // 4)
        playoff_limit = direct_limit + max(1, num_teams // 2)
        
    return render(request, 'tournament/standings.html', {
        'standings': table,
        'direct_limit': direct_limit,
        'playoff_limit': playoff_limit,
    })

@login_required
def matches(request):
    matches = Match.objects.all().order_by('round', 'match_date')
    return render(request, 'tournament/matches.html', {'matches': matches})

# Check if user is referee or admin
def is_referee_or_admin(user):
    return user.role in ['REFEREE', 'ADMIN', 'TEACHER'] or user.is_staff

@login_required
@user_passes_test(is_referee_or_admin)
def match_edit(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    
    # Validation: If match is already FINISHED, only Admin can edit
    if match.status == 'FINISHED' and not request.user.is_superuser:
        messages.error(request, "Este acta ya está cerrada y validada. No se puede modificar.")
        return redirect('matches')

    if request.method == 'POST':
        try:
            home_score = int(request.POST.get('home_score'))
            away_score = int(request.POST.get('away_score'))
            status = request.POST.get('status')
            
            match.home_score = home_score
            match.away_score = away_score
            match.status = status
            match.save()
            
            if status == 'FINISHED':
                messages.success(request, f"Partido {match} FINALIZADO y acta cerrada.")
            else:
                messages.success(request, f"Partido {match} actualizado correctamente.")
            return redirect('matches')
        except ValueError:
            messages.error(request, "Error en los datos introducidos.")
            
    return render(request, 'tournament/match_edit.html', {'match': match})

def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    players = team.players.all().order_by('dorsal')
    return render(request, 'tournament/team_detail.html', {'team': team, 'players': players})
