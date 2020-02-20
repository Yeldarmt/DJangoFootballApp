# Generated by Django 2.0 on 2020-02-19 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('season', models.CharField(default=None, max_length=100)),
                ('logo', models.ImageField(blank=True, upload_to=None)),
                ('seasonStart', models.DateTimeField(default=None)),
                ('seasonEnd', models.DateTimeField(default=None)),
                ('country', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='country.Country')),
            ],
        ),
    ]
