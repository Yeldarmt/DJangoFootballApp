from django.contrib import admin

# Register your models here.
from football_app.team.models import Team


# admin.site.register(Team)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_code', 'nick_name', 'lasts_5', 'coach', 'league')
