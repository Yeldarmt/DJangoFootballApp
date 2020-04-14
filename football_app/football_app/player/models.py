from django.db import models
from football_app.person.models import Person
from football_app.statistica.models import Statistica
from football_app.team.models import Team


# Create your models here.


class Player(Person):
    PLAYER_POSITIONS = (
        ('GK', 'Goalkeeper'),
        ('CB', 'Centre-back'),
        ('LB', 'Left-back'),
        ('RB', 'Right-back'),
        ('CM', 'Central midfield'),
        ('LM', 'Left midfield'),
        ('RM', 'Right midfield'),
        ('AM', 'Attacking midfield'),
        ('LW', 'Left winger'),
        ('RW', 'Right winger'),
        ('FC', 'Centre Forward'),
    )
    age = models.IntegerField()
    date_of_birth = models.DateField()
    photo = models.ImageField(
        default='https://www.doughroller.net/wp-content/uploads/2018/06/soccer-stars-648x364-c-default.jpg',
        upload_to='photos/')
    height = models.FloatField()
    weight = models.FloatField()
    position = models.CharField(max_length=2, choices=PLAYER_POSITIONS)
    number = models.IntegerField()
    salary = models.IntegerField()
    isReserved = models.BooleanField(default=False)
    statistica = models.OneToOneField(Statistica, on_delete=models.CASCADE, related_name='statistics')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

    def __str__(self):
        return '{} {}'.format(self.surname, self.name)
