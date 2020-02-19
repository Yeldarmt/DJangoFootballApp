from django.db import models

# Create your models here.


class Statistica(models.Model):
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    red_card = models.IntegerField(default=0)
    yellow_card = models.IntegerField(default=0)
    played_games = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'statistic'
        verbose_name_plural = 'statistics'

    def __str__(self):
        return '{} and {} in {} matches'.format(self.goals, self.assists, self.played_games)