# Generated by Django 2.0 on 2020-02-13 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_auto_20200214_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='photo',
            field=models.ImageField(default='https://www.doughroller.net/wp-content/uploads/2018/06/soccer-stars-648x364-c-default.jpg', upload_to='photos/'),
        ),
    ]