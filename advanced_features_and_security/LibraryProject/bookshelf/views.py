from django.shortcuts import render,redirect# Create your views here.
from django.contrib.auth.decorators import permission_required, MyModel


@permission_required('app_name.view_mymodel', raise_exception=True)
def view_mymodel(request, pk):
    # Fetch MyModel instance
    mymodel = MyModel.objects.get(pk=pk)
    # ... (process and display MyModel data)
    return render(request, 'view_mymodel.html', {'mymodel': mymodel})

@permission_required('app_name.create_mymodel', raise_exception=True)
def create_mymodel(request):
    if request.method == 'POST':
        # ... (validate and save new MyModel instance)
        return redirect('success_url')  # Replace with appropriate redirect URL
    # ... (display form for creating MyModel)
    return render(request, 'create_mymodel.html')


from django.shortcuts import render, get_object_or_404

from .models import Book  # Assuming Book model is defined in models.py

def book_list(request):
    books = Book.objects.all()  # Fetch all books
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)  # Get book by primary key (pk)
    return render(request, 'book_detail.html', {'book': book})