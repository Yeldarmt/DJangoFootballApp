from django.db import models
from football_app.referee.models import Referee
from football_app.team.models import Team


class GamesManager(models.Manager):
    def get_queryset(self):
        return super(GamesManager, self).get_queryset().all()


class ActiveGamesManager(models.Manager):
    def get_queryset(self):
        return super(ActiveGamesManager, self).get_queryset().filter(isActiveGame=True)


class NotActiveGamesManager(models.Manager):
    def get_queryset(self):
        return super(NotActiveGamesManager, self).get_queryset().filter(isActiveGame=False)


class Game(models.Model):
    game_date = models.DateTimeField()
    score_team_one = models.IntegerField(default=0)
    score_team_second = models.IntegerField(default=0)
    stadium = models.CharField(max_length=200)
    isActiveGame = models.BooleanField(default=False)
    first_team = models.ForeignKey(Team, on_delete=models.CASCADE, default=None, related_name='first_team')
    second_team = models.ForeignKey(Team, on_delete=models.CASCADE, default=None, related_name='second_team')
    referee = models.ForeignKey(Referee, on_delete=models.CASCADE)
    objects = GamesManager()
    active_games = ActiveGamesManager()
    not_active_games = NotActiveGamesManager()

    class Meta:
        verbose_name: 'Game'
        verbose_name_plural: 'Games'

    def __str__(self):
        return '{} - {}'.format(self.first_team.short_code, self.second_team.short_code)
