from .models import Book

book = Book.objects.get(title="1984")  # Or use book.id if preferred

print("Book details:")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")