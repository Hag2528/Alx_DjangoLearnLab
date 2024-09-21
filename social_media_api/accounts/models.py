from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(blank=True,null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
    
#task2 week 15
from django.db import models

class User(models.Model):
    # Existing user fields (username, email, etc.)
    following = models.ManyToManyField('self', symmetrical=False, blank=True)

