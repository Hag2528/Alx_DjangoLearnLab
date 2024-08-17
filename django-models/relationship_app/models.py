from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField()
class Book(models.Model):
    title=models.CharField()
    Author=models.ForeignKey(Author,on_delete=models.CASCADE)
class Library(models.Model):
    name=models.CharField()
    books=models.ManyToManyField(Book, related_name='books')
