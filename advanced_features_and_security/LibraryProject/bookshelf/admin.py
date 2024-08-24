from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

# Register your models here.
from .models import Book  # Import the Book model

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Customize list view
    list_filter = ('author', 'publication_year')  # Add list filters
    search_fields = ('title', 'author')  # Enable searching

admin.site.register(Book, BookAdmin)

class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Personal Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)