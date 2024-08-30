from django.db import models

# Create your models here.class 
class Book(models.Model):
    titl=models.CharField()
    author=models.CharField()