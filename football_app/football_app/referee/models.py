from django.db import models
from football_app.person.models import Person

# Create your models here.


class Referee(Person):
    level = models.CharField(max_length=200)
    salary = models.IntegerField()

    class Meta:
        verbose_name: 'Referee'
        verbose_name_plural: 'Refereessa'

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)

