from django.contrib import admin
from football_app.game.models import Game

# Register your models here.


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_team', 'second_team', 'game_date', 'isActiveGame', 'referee', )
