from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Book(models.Model):
    # Existing book model fields

    class Meta:
        permissions = [
            ("can_add_book", "Can Add Book"),
            ("can_change_book", "Can Change Book"),
            ("can_delete_book", "Can Delete Book"),
        ]




from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Role(models.Model):
    """Model for predefined user roles."""
    ADMIN = 'admin'
    LIBRARIAN = 'librarian'
    MEMBER = 'member'
    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (LIBRARIAN, 'Librarian'),
        (MEMBER, 'Member'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, unique=True)

    def __str__(self):
        return self.role


class UserProfile(models.Model):
    """Model for user profiles with a one-to-one relationship with User."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)   


    def __str__(self):
        return f"{self.user.username} ({self.role})"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Automatically creates a UserProfile instance when a new User is registered."""
    if created:
        UserProfile.objects.create(user=instance)




# class Role(models.Model):
#     ADMIN = 'admin'
#     LIBRARIAN ='librarian'
#     MEMBER = 'member'
#     ROLE_CHOICES = (
#         (ADMIN, 'Admin'),
#         (LIBRARIAN, 'Librarian'),
#         (MEMBER, 'Member'),
#     )

#     role = models.CharField(max_length=50, choices=ROLE_CHOICES, default=MEMBER)
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#     role = models.CharField(max_length=10, choices=Role.choices,default=Role.MEMBER)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
# signals.post_save.connect(create_user_profile, sender= User) 

# class Author(models.Model):
#   name = models.CharField(max_length=100)
#    return self.name
# class Book(models.Model):
#  title = models.CharField()
#  author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')   

# class Library(models.Model):
#   name = models.CharField(max_length=100)   
#   books = models.ManyToManyField(Book,related_name='libraries')


# class Librarian(models.Model):
#   name = models.CharField(max_length=100)
#   library = models.OneToOneField(Library, on_delete=models.CASCADE , related_name='libraries')

class Author(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class Book(models.Model):
 title = models.CharField(max_length=255)
 author = models.ForeignKey(Author, on_delete=models.CASCADE)
 def __str__(self):
    return self.title

class Library(models.Model):
  name = models.CharField(max_length=255) 


  def __str__(self):
    return self.name

class Librarian(models.Model):
  name = models.CharField(max_length=255)
  library = models.OneToOneField(Library, on_delete=models.CASCADE)

  def __str__(self):
    return self.name