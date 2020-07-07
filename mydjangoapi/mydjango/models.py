from django.db import models

# Create your models here.

class Content(models.Model):
    name = models.CharField(max_length=18)
    comment = models.CharField(max_length=140)
    def __str__(self):
        return self.name

class Goods(models.Model):
    name = models.CharField(max_length=18)
    description = models.CharField(max_length=140)
    price = models.IntegerField()
    image = models.URLField(default='')
    def __str__(self):
        return self.name
