#task one week 15
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all() 

    serializer_class = PostSerializer
    pagination_class = PageNumberPagination  
  # Add pagination

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user) 
  # Set author to current user

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if not user.is_staff:
            queryset = queryset.filter(author=user)  # Filter for authenticated user's posts
        return queryset

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination 
  # Add pagination

    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_object())  # Set author and post

    def get_object(self):
        pk = self.kwargs.get("pk")
        if not pk:
            raise serializers.ValidationError("Post ID is required.")
        return Post.objects.get(pk=pk)