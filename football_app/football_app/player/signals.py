from django.db.models.signals import post_save
from django.dispatch import receiver
import logging
from .models import Player, PlayerFullInfo

logger = logging.getLogger('main')


@receiver(post_save, sender=Player)
def user_created(sender, instance, created, **kwargs):
    if created:
        logger.debug(f'PlayerFUllInfo created for {instance}')
        logger.info(f'PlayerFUllInfo created for {instance}')
        logger.warning(f'PlayerFUllInfo created for {instance}')
        logger.error(f'PlayerFUllInfo created for {instance}')
        logger.critical(f'PlayerFUllInfo created for {instance}')
        PlayerFullInfo.objects.create(player=instance)
