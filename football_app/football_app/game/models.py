from django.db import models
from football_app.player.models import Player
from football_app.goal.models import Goal
from football_app.referee.models import Referee

# Create your models here.


class Game(models.Model):
    # first_team = models.ForeignKey(Player, on_delete=models.CASCADE)
    # second_team = models.ForeignKey(Player, on_delete=models.CASCADE)
    game_date = models.DateTimeField()
    goals = models.ForeignKey(Goal, on_delete=models.CASCADE)
    referee = models.ForeignKey(Referee, on_delete=models.CASCADE)
    score_team_one = models.IntegerField()
    score_team_second = models.IntegerField()
