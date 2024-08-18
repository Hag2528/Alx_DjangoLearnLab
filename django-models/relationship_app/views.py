# Create your views here.
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book , Library
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

def list_books(request):
    books = Book.objects.all()  # Fetch all books from database
    context = {'books': books}  # Create context dictionary
    return render(request, 'relationship_app/list_books.html', context)  # Render template

class LibraryDetailView(DetailView):
    model = Library  # Specify model for detail view
    template_name = 'library_detail.html'  # Set template name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()  # Retrieve current library object
        context['books'] = library.books.all()  # Get books associated with this library
        return context
def login_view(request):
    if request.method == 'POST':   
    login_form = AuthenticationForm(request, data=request.POST)
    if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']   

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('relationship_app:home')   
  # Redirect to your app's home page
            else:
                # Handle invalid login credentials (avoid revealing specific errors)
                login_form.add_error(None, 'Invalid username or password.')
    else:
        login_form = AuthenticationForm()
    context = {'login_form': login_form}
    return render(request, 'relationship_app/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('relationship_app:login')  # Redirect to login page

def register_view(request):
    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request,user)  # Log in the user automatically after registration (optional)
            return redirect('relationship_app:home')
    else:
        register_form = UserCreationForm()
    context = {'register_form': register_form}
    return render(request, 'relationship_app/register.html', context)


