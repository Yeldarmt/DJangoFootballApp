from django.db import models
from football_app.person.models import Person
from football_app.statistica.models import Statistica
from football_app.team.models import Team
import logging
import os
from django.core.exceptions import ValidationError

logger = logging.getLogger('main')


MAX_FILE_SIZE = 1024000
ALLOWED_EXTENSIONS = ['.pdf', '.docx']


def validate_file_size(value):
    print('size', value.size)
    if value.size > MAX_FILE_SIZE:
        logger.debug(f'File size more than {MAX_FILE_SIZE}, current file size: {value.size}')
        logger.info(f'File size more than {MAX_FILE_SIZE}, current file size: {value.size}')
        logger.warning(f'File size more than {MAX_FILE_SIZE}, current file size: {value.size}')
        logger.error(f'File size more than {MAX_FILE_SIZE}, current file size: {value.size}')
        logger.critical(f'File size more than {MAX_FILE_SIZE}, current file size: {value.size}')
        raise ValidationError(f'max file size is: {MAX_FILE_SIZE}')
    else:
        logger.debug(f'File added to PlayerFileInfo, with file size:{value.size}')
        logger.info(f'File added to PlayerFileInfo, with file size:{value.size}')
        logger.warning(f'File added to PlayerFileInfo, with file size:{value.size}')
        logger.error(f'File added to PlayerFileInfo, with file size:{value.size}')
        logger.critical(f'File added to PlayerFileInfo, with file size:{value.size}')


def validate_extension(value):
    split_ext = os.path.splitext(value.name)
    if len(split_ext) > 1:
        ext = split_ext[1]
        if not ext.lower() in ALLOWED_EXTENSIONS:
            logger.debug(f'not allowed file, valid extensions: {ALLOWED_EXTENSIONS}')
            logger.info(f'not allowed file, valid extensions: {ALLOWED_EXTENSIONS}')
            logger.warning(f'not allowed file, valid extensions: {ALLOWED_EXTENSIONS}')
            logger.error(f'not allowed file, valid extensions: {ALLOWED_EXTENSIONS}')
            logger.critical(f'not allowed file, valid extensions: {ALLOWED_EXTENSIONS}')
            raise ValidationError(f'not allowed file, valid extensions: {ALLOWED_EXTENSIONS}')
        else:
            logger.debug(f'file validated, file extension: {ext.lower()}')
            logger.info(f'file validated, file extension: {ext.lower()}')
            logger.warning(f'file validated, file extension: {ext.lower()}')
            logger.error(f'file validated, file extension: {ext.lower()}')
            logger.critical(f'file validated, file extension: {ext.lower()}')


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
    statistica = models.OneToOneField(Statistica, on_delete=models.CASCADE, related_name='statistics', null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    objects = PlayerManager()
    not_res_players = NotReservedPlayersManager()
    res_players = ReservedPlayersManager()

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

    def __str__(self):
        return '{} {}'.format(self.surname, self.name)

    def _try_create_profile_for_player(self, created):
        print('not in _try_create_profile_for_player', self)
        if created:
            print('in _try_create_profile_for_player')
            PlayerFullInfo.objects.get_or_create(player=self)
        else:
            logger.debug(f'Player: {self} data was changed!')
            logger.info(f'Player: {self} data was changed!')
            logger.warning(f'Player: {self} data was changed!')
            logger.error(f'Player: {self} data was changed!')
            logger.critical(f'Player: {self} data was changed!')

    def save(self, *args, **kwargs):
        print('before saving')

        created = self.id is None

        super(Player, self).save(*args, **kwargs)

        self._try_create_profile_for_player(created)

        print('after saving')


class PlayerFullInfo(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE, null=True, blank=True)
    player_info = models.FileField(upload_to='files', null=True, blank=True,
                                   validators=[validate_file_size, validate_extension])
