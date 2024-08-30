from django.db import models

# Create your models here.class 
class Book(models.Model):
    title=models.CharField()
    author=models.CharField()