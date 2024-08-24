from .models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()

print("Book created successfully!")

booka = Book.objects.get(title="1984")  # Or use book.id if preferred

print("Book details:")
print(f"Title: {booka.title}")
print(f"Author: {booka.author}")
print(f"Publication Year: {booka.publication_year}")

bookb = Book.objects.get(title="1984")
bookb.title = "Nineteen Eighty-Four"
bookb.save()

print("Book title updated successfully!")

bookc = Book.objects.get(title="Nineteen Eighty-Four")
bookc.delete()

print("Book deleted successfully!")

# Confirm deletion
books = Book.objects.all()
if not books.exists():
    print("No books found. Deletion confirmed.")
else:
    print("Error: Book deletion failed!")