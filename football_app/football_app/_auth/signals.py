from django.db.models.signals import post_save
from django.dispatch import receiver

from football_app._auth.models import Notification
from football_app.game.models import Game


@receiver(post_save, sender=Game)
def game_created(sender, instance, created, **kwargs):
    if created:
        f_team=instance.first_team
        s_team=instance.second_team
        f_users=f_team.subscribers.all()
        s_users=s_team.subscribers.all()


        for user in f_users:
            Notification.objects.create(user=user,game=instance)

        for user in s_users:
            Notification.objects.create(user=user, game=instance)

