from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('register/',views.register.as_view("LogoutView.as_view(template_name=", "LoginView.as_view(template_name=")),
    path('logout/', views.logout_view, name='logout'),
    path('books/', views.list_books, name='book_list'),
    # path('libraries/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

    path('add-book/', views.add_book, name='add_book'),
    path('edit-book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete-book/<int:book_id>/', views.delete_book, name='delete_book'),
]