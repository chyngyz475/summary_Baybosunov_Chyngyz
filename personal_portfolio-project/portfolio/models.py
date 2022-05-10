from distutils.command.upload import upload
from turtle import update
from django.db import models

# Create your models here.
class Project(models.Model):
    url_height=models.PositiveIntegerField()
    url_width=models.PositiveIntegerField()
    image = models.ImageField(upload_to='portfolio/images/', height_field='url_height', width_field='url_width')
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=2000)
    url = models.URLField(blank=True)
    
    
    def __str__(self):
        return self.title