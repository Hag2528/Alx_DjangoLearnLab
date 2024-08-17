from relationship_app.models import Author, Book, Library, Librarian
def get_books_by_author(author_name):
  books=Book.objects.get(name=author_name)
  return Book.objects.filter(author=books)

def get_books_in_library(library_name):
  library = Library.objects.get(name=library_name)
  return library.books.all()

def get_librarian_for_library(library_name):
  library = Library.objects.get(name=library_name)
  return library.librarian
