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





#task3   week 15

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from notifications.models import Notification
from .models import Post, Like
from django.contrib.contenttypes.models import ContentType
@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if Like.objects.filter(post=post, user=request.user).exists():
        messages.info(request, 'You already liked this post.')
    else:
        like = Like.objects.create(post=post, user=request.user)
        # Generate notification for the post owner (optional)
        if post.user != request.user:
            Notification.objects.create(
                recipient=post.user,
                actor=request.user,
                verb='liked your post',
                target_content_type=ContentType.objects.get_for_model(Post),
                target_object_id=post.id
            )
        messages.success(request, 'Post liked!')

    return redirect('post_detail', pk=post.pk)

@login_required
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like = Like.objects.filter(post=post, user=request.user).first()

    if like:
        like.delete()
        messages.success(request, 'Post unliked.')
    else:
        messages.info(request, 'You did not like this post.')

    return redirect('post_detail', pk=post.pk)