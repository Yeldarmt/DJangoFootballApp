# Generated by Django 2.0 on 2020-02-16 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='score_team_one',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='score_team_second',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]