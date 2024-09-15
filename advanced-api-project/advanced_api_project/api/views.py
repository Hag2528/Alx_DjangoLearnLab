from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .models import Book
from .serializers import BookSerializer


# Step 1: Set Up Generic Views with Customizations

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny] 
  # Allow read-only access for everyone

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
  # Allow read-only access for everyone

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
  # Restrict to authenticated users

    def post(self, request, *args, **kwargs):
        # Custom validation (optional)
        if 'title' not in request.data or request.data['title'] == '':
            raise ValidationError({'title': 'This field is required.'})

        return super().post(request, *args, **kwargs)

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
  # Restrict to authenticated users

    def put(self, request, *args, **kwargs):
        # Custom validation (optional)
        # ... (similar to BookCreateView)

        return super().put(request, *args, **kwargs)

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 

    permission_classes = [permissions.IsAuthenticated] 
  # Restrict to authenticated users


from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView): 

    """
    List view for retrieving all Book objects.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Allow read-only access for all users

class BookDetailView(generics.RetrieveAPIView):
    """
    Detail view for retrieving a single Book object by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Allow read-only access for all users

class BookCreateView(generics.CreateAPIView):
    """
    Create view for adding a new Book object.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Restrict to authenticated users

class BookUpdateView(generics.UpdateAPIView):
    """
    Update view for modifying an existing Book object.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Restrict to authenticated users

class BookDeleteView(generics.DestroyAPIView):
    """
    Delete view for removing a Book object.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] 