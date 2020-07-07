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
    date = models.DateTimeField(default=timezone.now)
    icon = models.TextField(default="@/assets/cat.jpg")
    def __str__(self):
        return self.name
