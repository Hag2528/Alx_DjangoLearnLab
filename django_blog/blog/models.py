# from django.db import models
# from django.contrib.auth.models import User
# # Create your models here.
# class Post(models.Model):
#  title=models.CharField(max_length=200)
#  content=models.TextField()
#  published_date= models.DateTimeField(auto_now_add=True)
#  author= models.ForeignKey(User,related_name="Post")
# #3
from django.contrib.auth.models import User
from django.db import models
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return self.user.username



# from django.db import models
# from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)

    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User model
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    # Consider adding additional fields like category, tags, etc.

    def __str__(self):
        return self.title
    
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Post(models.Model):

    # ... other fields ...
    tags = models.ManyToManyField(Tag)


from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name 
from django.db import models

class Post(models.Model):
    # ... other fields
    tags = models.ManyToManyField(Tag)