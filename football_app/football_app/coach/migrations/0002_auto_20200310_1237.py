# Generated by Django 2.0 on 2020-03-10 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='age',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='coach',
            name='salary',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
