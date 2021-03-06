# Generated by Django 3.0.5 on 2020-04-25 14:15

from django.db import migrations, models
import django.db.models.deletion
import football_app.goal.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('player', '0001_initial'),
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recordTime', models.IntegerField(validators=[football_app.goal.models.valid_recordTime])),
                ('assistPlayer', models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='assist_player', to='player.Player')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Game')),
                ('goalPlayer', models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='goal_player', to='player.Player')),
            ],
        ),
    ]
