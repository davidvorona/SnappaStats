from django.contrib import admin

from .models import Profile, Game, DigestedStats, Player, Team

admin.site.register(Profile)
admin.site.register(Game)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(DigestedStats)
