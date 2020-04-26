from django.contrib import admin
from football_app.player.models import Player, PlayerFullInfo

# Register your models here.


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'name', 'date_of_birth', 'position', 'isReserved', 'nationality')


@admin.register(PlayerFullInfo)
class PlayerFullInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'player', )