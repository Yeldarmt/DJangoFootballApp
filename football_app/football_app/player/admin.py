from django.contrib import admin
from football_app.player.models import Player

# Register your models here.


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'name', 'date_of_birth', 'position', 'team')
