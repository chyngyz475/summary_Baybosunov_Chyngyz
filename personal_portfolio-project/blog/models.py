from itertools import chain
from pyexpat import model
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    date  = models.DateField()
    text = models.TextField(max_length=150)
    
    def __str__(self):
        return self.title
