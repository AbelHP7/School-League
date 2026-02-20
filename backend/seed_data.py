import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from tournament.models import Team, Player, Match

TEAMS_DATA = [
    # Grupo A
    ("Real Madrid", "Carlo Ancelotti"),
    ("FC Barcelona", "Xavi Hernández"),
    ("Atlético de Madrid", "Diego Simeone"),
    ("Sevilla FC", "Quique Sánchez Flores"),
    # Grupo B
    ("Real Betis", "Manuel Pellegrini"),
    ("Athletic Club", "Ernesto Valverde"),
    ("Real Sociedad", "Imanol Alguacil"),
    ("Villarreal CF", "Marcelino"),
    # Grupo C
    ("Valencia CF", "Rubén Baraja"),
    ("Girona FC", "Míchel"),
    ("CA Osasuna", "Jagoba Arrasate"),
    ("Celta de Vigo", "Claudio Giráldez"),
    # Grupo D
    ("Rayo Vallecano", "Iñigo Pérez"),
    ("RCD Mallorca", "Javier Aguirre"),
    ("Deportivo Alavés", "Luis García Plaza"),
    ("UD Las Palmas", "García Pimienta")
]

FIRST_NAMES = ["Lamine", "Ayoze", "Nico", "Iñaki", "Rodrygo", "Vinícius", "Luka", "Antoine", "Álvaro", "Koke", "Marcos", "Brahim", "Joselu", "Gavi", "Pedri"]
LAST_NAMES = ["Yamal", "Pérez", "Williams", "Modric", "Griezmann", "Morata", "Llorente", "Bellingham", "Araujo", "Kroos", "Valverde", "Oyarzabal", "Merino", "Aspas"]

def seed_db():
    print("Iniciando generación masiva de datos (16 equipos)...")
    
    # 1. Clear old data completely to avoid mix-ups
    Match.objects.all().delete()
    Team.objects.all().delete()
    print("Mesa limpiada (antiguos partidos, equipos y jugadores eliminados).")

    # 2. Create Teams and Players
    for index, (team_name, coach) in enumerate(TEAMS_DATA):
        team = Team.objects.create(name=team_name, coach=coach)
        
        # Add 11 random players to each team
        for i in range(1, 12):
            player_name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
            Player.objects.create(name=player_name, dorsal=i, team=team)
            
    print(f"¡Generación Completada! Se han creado {Team.objects.count()} equipos y {Player.objects.count()} jugadores.")

if __name__ == '__main__':
    seed_db()
