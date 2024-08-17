# Create your views here.
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library,Book 

def list_books(request):
    books = Book.objects.all() 
    book_list = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return render(request, 'list_books.html', {'books': book_list})  # Render with context


class LibraryDetailView(DetailView):
    model = Library  # Specify model for DetailView
    template_name = 'library_detail.html'  # Template for rendering

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['books'] = self.object.books.all()  # Get books related to the library
    return context