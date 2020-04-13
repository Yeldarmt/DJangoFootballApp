from django.db import models
from football_app.referee.models import Referee
from football_app.team.models import Team


class Game(models.Model):
    game_date = models.DateTimeField()
    score_team_one = models.IntegerField(default=0)
    score_team_second = models.IntegerField(default=0)
    stadium = models.CharField(max_length=200)
    isActiveGame = models.BooleanField(default=False)
    first_team = models.ForeignKey(Team, on_delete=models.CASCADE, default=None, related_name='first_team')
    second_team = models.ForeignKey(Team, on_delete=models.CASCADE, default=None, related_name='second_team')
    referee = models.ForeignKey(Referee, on_delete=models.CASCADE)

    class Meta:
        verbose_name: 'Game'
        verbose_name_plural: 'Games'

    def __str__(self):
        return '{} {}'.format(self.first_team.short_code, self.second_team.short_code)
