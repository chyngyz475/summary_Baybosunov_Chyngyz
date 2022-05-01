from itertools import chain
from pyexpat import model
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    data  = models.DateField()
    text = models.CharField(max_length=150)
