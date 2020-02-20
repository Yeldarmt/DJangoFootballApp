from django.db import models

from football_app.person.models import Person


class Coach(Person):
    age=models.IntegerField(default=0)
    height=models.FloatField(default=0)
    weight=models.FloatField(default=0)
    date_of_birth=models.DateField(default=None)
    salary=models.IntegerField(default=0)
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'nationality': self.nationality,
            'age': self.age,
            'height': self.height,
            'weight': self.weight,
            'date_of_birth': self.date_of_birth,
            'salary': self.salary
        }

    def __str__(self):
        return '{} {}'.format(self.surname,self.name)
