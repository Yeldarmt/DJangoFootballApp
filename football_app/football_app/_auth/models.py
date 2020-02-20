from django.db import models
from django.contrib.auth.models import AbstractUser

from football_app.team.models import Team


class MyUser(AbstractUser):
    address = models.CharField(max_length=50,default='')
    #favouriteTeam=models.ForeignKey(Team,on_delete=models.CASCADE,default=1)
    #favouriteMatches=models.ForeignKey(Matches,on_delete=models.CASCADE)
    birth_date=models.DateField(null=True,blank=True)

    def to_json(self):
        return {
            'username ': self.username,
            'first_name': self.first_name,
            'last_name' : self.last_name,
            'email ': self.email,
            'address' :self.address,
            'favouriteTeam':self.favouriteTeam,
            'birth_date':self.birth_date
        }

    def __str__(self):
        return 'username: {}, Full name: {}'.format(self.username,self.get_full_name())