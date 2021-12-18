from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=400)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modifed = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

class Category(models.Model):
    name = models.CharField(max_length=50)

class Comment(models.Model):
    author = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)