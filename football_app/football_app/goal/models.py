from django.db import models
from football_app.player.models import Player
from football_app.game.models import Game
from rest_framework import serializers


def valid_recordTime(value):
    print('valid_recordTime')
    if 1 > value > 120:
        raise serializers.ValidationError('error: goals can be added only in game time')
    return value


class Goal(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    recordTime = models.IntegerField(validators=[valid_recordTime])
    goalPlayer = models.ForeignKey(Player, on_delete=models.CASCADE, default=4, related_name='goal_player')
    assistPlayer = models.ForeignKey(Player, on_delete=models.CASCADE, default=5, related_name='assist_player')

    class Meta:
        verbose_name: 'Goal'
        verbose_name_plural: 'Goals'

    def __str__(self):
        return '{} {}'.format(self.goalPlayer.name, self.goalPlayer.surname)

    def add_goaler_goal(self, player):
        goaler_stata = player.statistica
        goaler_stata.goals = goaler_stata.goals + 1
        goaler_stata.save()
        player.save()

    def add_assist(self, assistent):
        assistent_stata = assistent.statistica
        assistent_stata.assists = assistent_stata.assists + 1
        assistent_stata.save()
        assistent.save()
