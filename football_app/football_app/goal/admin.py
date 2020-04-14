from django.contrib import admin
from football_app.goal.models import Goal

# Register your models here.


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('id', 'game', 'recordTime', 'goalPlayer', 'assistPlayer')
