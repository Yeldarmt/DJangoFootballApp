from django.db import models
from django.db import models
# Create your models here.

class Country(models.Model):
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=100,default=None,blank=True)
    flag= models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'flag': self.flag
        }

    def __str__(self):
        return '{} '.format(self.name)