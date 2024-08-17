# Create your views here.
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book , Library

def list_books(request):
    books = Book.objects.all()  # Fetch all books from database
    context = {'books': books}  # Create context dictionary
    return render(request, 'list_books.html', context)  # Render template

class LibraryDetailView(DetailView):
    model = Library  # Specify model for detail view
    template_name = 'library_detail.html'  # Set template name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()  # Retrieve current library object
        context['books'] = library.books.all()  # Get books associated with this library
        return context

