from django.contrib import admin
from football_app.statistica.models import Statistica

# Register your models here.


@admin.register(Statistica)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('goals', 'assists', 'played_games')
