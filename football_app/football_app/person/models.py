from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)

    class Meta:
        abstract = True
