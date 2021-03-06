# Generated by Django 3.0.5 on 2020-04-25 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
        ('referee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_date', models.DateTimeField()),
                ('score_team_one', models.IntegerField(default=0)),
                ('score_team_second', models.IntegerField(default=0)),
                ('stadium', models.CharField(max_length=200)),
                ('isActiveGame', models.BooleanField(default=False)),
                ('first_team', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='first_team', to='team.Team')),
                ('referee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='referee.Referee')),
                ('second_team', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='second_team', to='team.Team')),
            ],
        ),
    ]
