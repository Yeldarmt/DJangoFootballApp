from django.contrib import admin
from football_app.referee.models import Referee
# Register your models here.


@admin.register(Referee)
class RefereeAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', )
