from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='book_list'),
    path('libraries/', views.LibraryDetailView.as_view(), name='library_detail'),
]