from django.db import models
from django.db.models.base import Model

# Create your models here.
# Project showcase 
# ohh yaha par sabse pahle aana tha project folder par

class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")
