from django.db import models
from django.utils import timezone
import datetime


# Create your models here.

class Content(models.Model):
    name = models.CharField(max_length=18)
    comment = models.CharField(max_length=140)
    regi_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
