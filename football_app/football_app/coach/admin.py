from django.contrib import admin

from football_app.coach.models import Coach


# admin.site.register(Coach)

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'nationality')
