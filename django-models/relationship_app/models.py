from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Role(models.Model):
    ADMIN = 'admin'
    LIBRARIAN ='librarian'
    MEMBER = 'member'
    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (LIBRARIAN, 'Librarian'),
        (MEMBER, 'Member'),
    )

    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default=MEMBER)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=Role.choices,default=Role.MEMBER)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
# signals.post_save.connect(create_user_profile, sender= User) 

class Author(models.Model):
  name = models.CharField(max_length=100)

class Book(models.Model):
 title = models.CharField()
 author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')   

class Library(models.Model):
  name = models.CharField(max_length=100)   
  books = models.ManyToManyField(Book,related_name='libraries')


class Librarian(models.Model):
  name = models.CharField(max_length=100)
  library = models.OneToOneField(Library, on_delete=models.CASCADE , related_name='libraries')

