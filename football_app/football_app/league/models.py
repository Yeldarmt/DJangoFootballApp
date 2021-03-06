from datetime import datetime
from football_app.country.models import Country
from django.db import models


# Create your models here.


class League(models.Model):
    name = models.CharField(max_length=100)
    season = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(default='https://toplogos.ru/images/logo-uefa-champions-league.jpg', upload_to='photos/')
    seasonStart = models.DateTimeField(null=True, blank=True)
    seasonEnd = models.DateTimeField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=None, related_name="leagues")

    def __str__(self):
        return '{} '.format(self.name)
