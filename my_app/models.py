from turtle import title
from django.db import models 
from datetime import datetime
from django.utils import timezone
from turtle import title



# Create your models here.

class Sam (models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

  