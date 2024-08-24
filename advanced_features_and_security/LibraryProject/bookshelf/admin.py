from django.contrib import admin

# Register your models here.
from .models import Book  # Import the Book model

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Customize list view
    list_filter = ('author', 'publication_year')  # Add list filters
    search_fields = ('title', 'author')  # Enable searching

admin.site.register(Book, BookAdmin)