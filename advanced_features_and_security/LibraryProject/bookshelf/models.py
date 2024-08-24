from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager,PermissionsMixin
# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    publication_year=models.IntegerField()


class CustomUser(AbstractUser):
     date_of_birth = models.DateField()
     profile_photo = models.ImageField(upload_to='profile_photos/', blank=True)
    
class CustomUserManager(BaseUserManager):
  
    def create_user(self, email, password, date_of_birth, profile_photo=None):
       
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,

            profile_photo=profile_photo,
        )
        user.set_password(password)
        self.save(user, self._db)
        return user

    def create_superuser(self, email, password, date_of_birth, profile_photo=None, **extra_fields):
        """
        Creates a new superuser with the same arguments as `create_user`,
        with superuser privileges granted.
        """
        user = self.create_user(email, password, date_of_birth, profile_photo=profile_photo)
        user.is_staff = True
        user.is_superuser = True
        user.save(self._db)
        return user


class CustomUser(AbstractUser):
    username = None  # Remove username field if not required
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True)

    USERNAME_FIELD = 'email'  # Set email as the unique identifier
    REQUIRED_FIELDS = ['date_of_birth']  # Add date_of_birth to required fields

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    

class MyModel(PermissionsMixin, models.Model):
    # Your model fields here (e.g., title, content)

    # Custom permissions for MyModel
    can_view = models.BooleanField(default=False, help_text="Can view instances of MyModel")
    can_create = models.BooleanField(default=False, help_text="Can create new instances of MyModel")
    can_edit = models.BooleanField(default=False, help_text="Can edit existing instances of MyModel")
    can_delete = models.BooleanField(default=False, help_text="Can delete instances of MyModel")

    class Meta:
        permissions = [
            ("view_mymodel", "Can view MyModel"),
            ("create_mymodel", "Can create MyModel"),
            ("edit_mymodel", "Can edit MyModel"),
            ("delete_mymodel", "Can delete MyModel"),
        ]

    def has_view_permission(self, user):
        """
        Custom method to check if a user has view permission for this instance.
        """
        return user.has_perm('app_name.view_mymodel') or self.can_view

    def has_create_permission(self, user):
        """
        Custom method to check if a user has create permission.
        """
        return user.has_perm('app_name.create_mymodel')