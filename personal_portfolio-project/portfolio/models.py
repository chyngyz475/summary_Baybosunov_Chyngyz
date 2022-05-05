from distutils.command.upload import upload
from turtle import update
from django.db import models

# Create your models here.
class Project(models.Model):
    image = models.ImageField(upload_to='portfolio/images/', height_field=None , width_field=None)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=2000)
    url = models.URLField(blank=True)
    
    
    def __str__(self):
        return self.title