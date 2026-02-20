from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Team, Player, Match, Standing

# 1. Custom User Admin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_superuser')
    
    # Remove 'groups' and 'user_permissions' from default fieldsets
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Role Info', {'fields': ('role',)}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Role Info', {'fields': ('role',)}),
    )

# 2. Team Admin
class PlayerInline(admin.TabularInline):
    model = Player
    extra = 1

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'coach', 'created_at')
    search_fields = ('name', 'coach')
    inlines = [PlayerInline]

# 3. Match Admin
@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status', 'home_score', 'away_score', 'referee')
    list_filter = ('status', 'match_date', 'location')
    search_fields = ('home_team__name', 'away_team__name')

# 4. Standing Admin (Read Only mostly)
@admin.register(Standing)
class StandingAdmin(admin.ModelAdmin):
    list_display = ('team', 'points', 'played', 'won', 'drawn', 'lost', 'goal_difference')
    ordering = ('-points', '-goals_for')
    list_filter = ('points',)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'dorsal', 'team')
    list_filter = ('team',)
