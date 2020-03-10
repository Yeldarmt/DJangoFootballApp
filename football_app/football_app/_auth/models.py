from django.db import models
from django.contrib.auth.models import AbstractUser

from football_app.game.models import Game
from football_app.team.models import Team


class MyUser(AbstractUser):
    address = models.CharField(max_length=50,default='')
    favouriteTeam=models.ForeignKey(Team,on_delete=models.CASCADE,blank=True,null=True)
    favouriteMatches=models.ForeignKey(Game,on_delete=models.CASCADE,blank=True,null=True)
    birth_date=models.DateField(null=True,blank=True)



    def __str__(self):
        return 'username: {}, Full name: {}'.format(self.username,self.get_full_name())