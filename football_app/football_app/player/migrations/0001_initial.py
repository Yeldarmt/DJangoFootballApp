# Generated by Django 2.0 on 2020-02-13 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('date_of_birth', models.DateTimeField()),
                ('photo', models.ImageField(default='https://www.doughroller.net/wp-content/uploads/2018/06/soccer-stars-648x364-c-default.jpg', upload_to='')),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('position', models.CharField(choices=[('GK', 'Goalkeeper'), ('CB', 'Centre-back'), ('LB', 'Left-back'), ('RB', 'Right-back'), ('CM', 'Central midfield'), ('LM', 'Left midfield'), ('RM', 'Right midfield'), ('AM', 'Attacking midfield'), ('LW', 'Left winger'), ('RW', 'Right winger'), ('FC', 'Centre Forward')], max_length=2)),
                ('number', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('isReserved', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Player',
                'verbose_name_plural': 'Players',
            },
        ),
    ]
