# Generated by Django 3.0.5 on 2020-04-25 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_playerfullinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerfullinfo',
            name='player_info',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
    ]
