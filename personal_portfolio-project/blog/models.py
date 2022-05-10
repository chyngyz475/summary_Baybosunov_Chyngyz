from itertools import chain
from pyexpat import model
from django.db import models

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to='portfolio/images/', height_field=None , width_field=None)
    title = models.CharField(max_length=100)
    date  = models.DateField()
    description = models.CharField(max_length=500)
    text = models.TextField(max_length=150000)
    
    def __str__(self):
        return self.title
