# Generated by Django 2.0 on 2020-02-16 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0004_player_statistica'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='statistica',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='statistica.Statistica'),
        ),
    ]
