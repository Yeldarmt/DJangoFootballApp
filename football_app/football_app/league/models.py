from football_app.country.models import Country
from django.db import models
# Create your models here.

class League(models.Model):
    name=models.CharField(max_length=100)
    season=models.CharField(max_length=100,default=None)
    logo= models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,blank=True)
    seasonStart=models.DateTimeField(default=None)
    seasonEnd = models.DateTimeField(default=None)
    country=models.ForeignKey(Country,on_delete=models.CASCADE,default=None)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'seasonStart':self.seasonStart,
            'seasonEnd': self.seasonEnd,
            'country': self.country,
            'code': self.code,
            'flag': self.flag
        }

    def __str__(self):
        return '{} '.format(self.name)