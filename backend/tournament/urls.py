from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clasificacion/', views.standings, name='standings'),
    path('partidos/', views.matches, name='matches'),
    path('partido/<int:match_id>/editar/', views.match_edit, name='match_edit'),
    path('registro/', views.signup, name='signup'),
    path('mi-perfil/', views.profile, name='profile'),
    path('generar-partidos/', views.generate_matches, name='generate_matches'),
    path('equipo/<int:team_id>/', views.team_detail, name='team_detail'),
]
