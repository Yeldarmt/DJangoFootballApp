from django.db import models
from football_app.player.models import Player

# Create your models here.


class Goal(models.Model):
    recordTime = models.IntegerField()
    goalPlayer = models.ForeignKey(Player, on_delete=models.CASCADE, default=4, related_name='goaler_player')
    assistPlayer = models.ForeignKey(Player, on_delete=models.CASCADE, default=5, related_name='assist_player')

    class Meta:
        verbose_name: 'Goal'
        verbose_name_plural: 'Goals'

    def __str__(self):
        return '{} {}'.format(self.goalPlayer.name, self.goalPlayer.surname)
