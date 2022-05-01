from distutils.command.upload import upload
from turtle import update
from django.db import models

# Create your models here.
class Project(models.Model):
    image = models.ImageField(upload_to='portfolio/images/')
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=250)
    url = models.URLField(blank=True)