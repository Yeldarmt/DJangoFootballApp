from django.db import models
from football_app.person.models import Person
from football_app.statistica.models import Statistica
from football_app.team.models import Team


class PlayerManager(models.Manager):
    def get_queryset(self):
        return super(PlayerManager, self).get_queryset().all()


class ReservedPlayersManager(models.Manager):
    def get_queryset(self):
        return super(ReservedPlayersManager, self).get_queryset().filter(isReserved=True)


class NotReservedPlayersManager(models.Manager):
    def get_queryset(self):
        return super(NotReservedPlayersManager, self).get_queryset().filter(isReserved=False)


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
        upload_to='photos/', null=True, blank=True)
    height = models.FloatField()
    weight = models.FloatField()
    position = models.CharField(max_length=2, choices=PLAYER_POSITIONS)
    number = models.IntegerField()
    salary = models.IntegerField()
    isReserved = models.BooleanField(default=False)
    statistica = models.OneToOneField(Statistica, on_delete=models.CASCADE, related_name='statistics')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    objects = PlayerManager()
    not_res_players = NotReservedPlayersManager()
    res_players = ReservedPlayersManager()

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

    def __str__(self):
        return '{} {}'.format(self.surname, self.name)
