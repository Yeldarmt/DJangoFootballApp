# Generated by Django 2.0 on 2020-03-07 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='logo',
            field=models.ImageField(default='https://images.alphacoders.com/105/1056501.jpg', upload_to='photos/'),
        ),
    ]