from django.db import models

from football_app.person.models import Person


class Coach(Person):
    age = models.PositiveSmallIntegerField(default=0)
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    date_of_birth = models.DateField(default=None)
    salary = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '{} {}'.format(self.surname, self.name)
