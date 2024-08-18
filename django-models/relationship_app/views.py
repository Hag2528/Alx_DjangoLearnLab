# Create your views here.
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library
from .models import Book
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import UserProfile
from django.contrib.auth.decorators import permission_required

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def admin_view(request):
    """View accessible only to users with the 'Admin' role."""
    if not request.user.is_authenticated:
        return render(request, 'login.html')  # Redirect to login if not authenticated

    @user_passes_test(lambda user: user.profile.role.role == 'admin')
    def decorated_view(request):
        # Admin-specific content here
        return render(request,'admin_view.html')

    return decorated_view(request)


def librarian_view(request):
    """View accessible only to users with the 'Librarian' role."""
    if not request.user.is_authenticated:
        return render(request, 'login.html')  # Redirect to login if not authenticated

    @user_passes_test(lambda user: user.profile.role.role == 'librarian')
    def decorated_view(request):
        # Librarian-specific content here
        return render(request,'librarian_view.html')

    return decorated_view(request)


def member_view(request):
    """View accessible only to users with the 'Member' role."""
    if not request.user.is_authenticated:
        return render(request, 'login.html')  # Redirect to login if not authenticated

    @user_passes_test(lambda user: user.profile.role.role == 'member')
    def decorated_view(request):
        # Member-specific content here
        return render(request,'member_view.html')

    return decorated_view(request)



@permission_required('relationship_app.can_add_book')
def add_book(request):
    # Logic for adding a book entry

 @permission_required('relationship_app.can_change_book')
 def edit_book(request, book_id):
    # Logic for editing a book entry

  @permission_required('relationship_app.can_delete_book')
  def delete_book(request, book_id):
    # Logic for deleting a book entry


#    def admin_view(request):
#     if not request.user.is_authenticated:
#         return render(request, 'login.html')  # Redirect to login if not authenticated
#     if not request.user.profile.role == 'admin':
#         return render(request, 'unauthorized.html')  # Handle unauthorized access
#     return render(request, 'admin_view.html', {'content': 'This is the Admin view'})
# def librarian_view(request):
#     # ... Same logic as admin_view ...
#     return render(request, 'librarian_view.html')

# def member_view(request):
#     # ... Same logic as admin_view ...
#     return render(request, 'member_view.html')

# @user_passes_test(lambda u: u.is_authenticated and u.profile.role == 'LIBRARIAN')
# def librarian_view(request):
#     return render(request, 'librarian_view.html', {'content': 'This is the Librarian view'})

# @user_passes_test(lambda u: u.is_authenticated and u.profile.role == 'MEMBER')
# def member_view(request):
#     return render(request, 'member_view.html', {'content': 'This is the Member view'})

   def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)   
  # Log in the newly created user
            return redirect('home')  # Redirect to your desired home page
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'relationship_app/register.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')   

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')   
  # Redirect to your home page
            else:
                # Handle invalid credentials with an error message
                context = {'form': form, 'error': 'Invalid username or password'}
                return render(request, 'relationship_app/login.html', context)
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'relationship_app/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout




# def list_books(request):
#     books = Book.objects.all()  # Fetch all books from database
#     context = {'books': books}  # Create context dictionary
#     return render(request, 'relationship_app/list_books.html', context)  # Render template

# class LibraryDetailView(DetailView):
#     model = Library  # Specify model for detail view
#     template_name = 'relationship_app/library_detail.html'  # Set template name

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         library = self.get_object()  # Retrieve current library object
#         context['books'] = library.books.all()  # Get books associated with this library
#         return context
# def login_view(request):
#     if request.method == 'POST':   
#     login_form = AuthenticationForm(request, data=request.POST)
#     if login_form.is_valid():
#             username = login_form.cleaned_data['username']
#             password = login_form.cleaned_data['password']   

#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('relationship_app:home')   
#   # Redirect to your app's home page
#             else:
#                 # Handle invalid login credentials (avoid revealing specific errors)
#                 login_form.add_error(None, 'Invalid username or password.')
#     else:
#         login_form = AuthenticationForm()
#     context = {'login_form': login_form}
#     return render(request, 'relationship_app/login.html', context)

# def logout_view(request):
#     logout(request)
#     return redirect('relationship_app:login')  # Redirect to login page

# def register_view(request):
#     if request.method == 'POST':
#         register_form = UserCreationForm(request.POST)
#         if register_form.is_valid():
#             user = register_form.save()
#             login(request,user)  # Log in the user automatically after registration (optional)
#             return redirect('relationship_app:home')
#     else:
#         register_form = UserCreationForm()
#     context = {'register_form': register_form}
#     return render(request, 'relationship_app/register.html', context)


