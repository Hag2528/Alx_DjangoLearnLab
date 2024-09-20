#task one week 15
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers
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
#task 2 week 15
from django.shortcuts import get_object_or_404
from accounts.models import User
# posts/views.py

def get_feed(request):
  user = get_object_or_404(User, pk=request.user.pk)
  following_posts = user.posts.filter(author__in=user.following.all()).order_by('-created_at')
  # Return the list of following_posts
  return following_posts