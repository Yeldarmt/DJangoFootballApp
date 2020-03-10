from django.db import models
from django.db import models
# Create your models here.

class CountryManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)

class Country(models.Model):
    objects=CountryManager()
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=100,default=None,blank=True)
    flag= models.ImageField(default='https://www.akorda.kz/upload/content_files/simbols/flag.png',upload_to='photos/')

    class Meta:
        verbose_name_plural="countries"

    def __str__(self):
        return '{} '.format(self.name)

