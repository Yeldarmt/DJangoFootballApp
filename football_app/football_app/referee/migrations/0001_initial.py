# Generated by Django 3.0.5 on 2020-04-25 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Referee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=200)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
