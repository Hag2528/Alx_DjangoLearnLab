# from django.urls import path
# from .views import Author, Book , Library, Librarian
# from django.contrib.auth.views import LogoutView
# from.import views

# urlpatterns = [
#     path("Author",Author.as_view(),name="register"),
#     path("Book",Book.as_view(),name="Book"),
#     path("Librarian",Librarian.as_view(),name="Librarian"),
#     path('books/', views.list_books, name='list_books'),
#     path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='book_list'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]