# Generated by Django 2.0 on 2020-03-07 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]