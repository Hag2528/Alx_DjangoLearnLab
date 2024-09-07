from django.db import models

# Create your models here.
class Author(models.Model):
  name=models.CharField()
class Book(models.Model):
  title=models.CharField()
  publication_year=models.IntegerField()
  author=models.ForeignKey(Author)