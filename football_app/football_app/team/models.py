from django.db import models

from football_app.coach.models import Coach
from football_app.league.models import League
from football_app.country.models import Country

class Team(models.Model):
    name=models.CharField(max_length=100,)
    position=models.IntegerField(default=0)
    logo= models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,blank=True)
    wins = models.IntegerField(default=0,blank=True)
    draws = models.IntegerField(default=0,blank=True)
    losts = models.IntegerField(default=0,blank=True)
    point=models.IntegerField(default=0,blank=True)
    lasts_5 = models.CharField(max_length=100,default='')
    coach=models.ForeignKey(Coach,on_delete=models.CASCADE,blank=True)
    goal_difference=models.IntegerField(default=0,blank=True)
    short_code=models.CharField(max_length=100,blank=True,default='')
    league=models.ForeignKey(League,on_delete=models.CASCADE,blank=True,default=None)
    country=models.ForeignKey(Country,on_delete=models.CASCADE,default=None)


    def to_json(self):
        return {

            'name': self.name,
            'position': self.position,
            'logo': self.logo,
            'wins': self.wins,
            'draws': self.draws,
            'losts': self.losts,
            'point': self.point,
            'last_5': self.lasts_5,
            'coach': self.coach,
            'goal_difference': self.goal_difference,
            'short_code': self.short_code,
            'league': self.league,
            'country': self.country

        }

    def __str__(self):
        return '{}'.format(self.name)