from django.shortcuts import render
from rest_framework import generics 
from .models import Book  # Assuming Book model is in the same app
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
  queryset = Book.objects.all()  # Get all books
  serializer_class = BookSerializer



from rest_framework import viewsets
from rest_framework.serializers import ModelSerializer
# Replace 'my_app.models.Book' with your actual Book model path
from api.models import Book
class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint for CRUD operations on Book model
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

