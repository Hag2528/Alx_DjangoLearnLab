from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/',BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/', BookCreateView.as_view(), name='book-create'),  # Note the trailing slash
    path('books/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]




