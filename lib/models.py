from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField('date published')
    content = models.TextField(max_length=5000)
    author= models.CharField(max_length=200)
