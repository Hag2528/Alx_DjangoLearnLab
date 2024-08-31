from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book  # Assuming Book model is in the same app
from .serializers import BookSerializer

class BookList(ListAPIView):
  queryset = Book.objects.all()  # Get all books
  serializer_class = BookSerializer