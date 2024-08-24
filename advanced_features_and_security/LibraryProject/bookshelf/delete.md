from bookshelf.models import Book
from .models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print("Book deleted successfully!")
books = Book.objects.all()
if not books.exists():
    print("No books found. Deletion confirmed.")
else:
    print("Error: Book deletion failed!")