import random
from datetime import timedelta, date, datetime, time
from .models import Match, Team

import random
from datetime import timedelta, date, datetime, time
from django.db import transaction
from .models import Match, Team

def generate_league_phase_matches():
    """
    Generates a Swiss-system style league phase where each team plays 8 matches (4 home, 4 away).
    Designed specifically for 16 teams.
    """
    if Match.objects.filter(phase='LEAGUE').exists():
        return 0, "La Fase Liga ya está generada."

    teams = list(Team.objects.all())
    if len(teams) != 16:
        return 0, f"Se necesitan exactamente 16 equipos para este formato (hay {len(teams)})."

    random.shuffle(teams)
    matches_created = 0
    start_datetime = datetime.combine(date.today(), time(10, 0))
    
    # Track assigned match counts per team
    home_matches_count = {team.id: 0 for team in teams}
    away_matches_count = {team.id: 0 for team in teams}
    played_pairs = set()

    # Generate 8 rounds
    with transaction.atomic():
        for round_num in range(1, 9):
            round_base_date = start_datetime + timedelta(weeks=round_num - 1)
            available_teams = list(teams)
            random.shuffle(available_teams)
            
            pairs_this_round = []
            
            while len(available_teams) >= 2:
                # Try to find a valid pair
                found_pair = False
                for i in range(len(available_teams)):
                    for j in range(i + 1, len(available_teams)):
                        t1 = available_teams[i]
                        t2 = available_teams[j]
                        
                        # Check if they haven't played and respect home/away limits
                        pair_id1 = tuple(sorted([t1.id, t2.id]))
                        if pair_id1 not in played_pairs:
                            if home_matches_count[t1.id] < 4 and away_matches_count[t2.id] < 4:
                                home, away = t1, t2
                                found_pair = True
                            elif home_matches_count[t2.id] < 4 and away_matches_count[t1.id] < 4:
                                home, away = t2, t1
                                found_pair = True
                                
                            if found_pair:
                                pairs_this_round.append((home, away))
                                played_pairs.add(pair_id1)
                                home_matches_count[home.id] += 1
                                away_matches_count[away.id] += 1
                                available_teams.remove(t1)
                                available_teams.remove(t2)
                                break
                    if found_pair:
                        break
                        
                if not found_pair:
                    # Fallback if generation gets stuck due to random constraints
                    return 0, "Fallo al generar calendario sin repeticiones. Inténtalo de nuevo."

            # Create matches for this round
            for i, (home, away) in enumerate(pairs_this_round):
                match_date = round_base_date + timedelta(hours=i*2)
                Match.objects.create(
                    home_team=home,
                    away_team=away,
                    match_date=match_date,
                    status='SCHEDULED',
                    round=round_num,
                    phase='LEAGUE'
                )
                matches_created += 1

    return matches_created, f"¡Fase Liga generada! {matches_created} partidos creados (8 por equipo)."
