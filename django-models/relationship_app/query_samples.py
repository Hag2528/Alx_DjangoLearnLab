from relationship_app.models import Author, Book, Library, Librarian
def get_books_by_author(author_name):
   Author=Author.objects.get(name=author_name)
   return Author.objects.filter(author=Author)

def get_books_in_library(library_name):
  library = Library.objects.get(name=library_name)
  return library.books.all()

def get_librarian_for_library(library_name):
  library = Library.objects.get(name=library_name)
  return library.librarian
