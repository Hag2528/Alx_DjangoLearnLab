from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import UserProfileForm  # Import your custom form

User = get_user_model()

def user_profile(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = UserProfileForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully!')
                return redirect('profile')
  # Redirect back to profile page
        else:
            form = UserProfileForm(instance=user)
        context = {'form': form}
        return render(request, 'accounts/profile.html', context)
    else:
        return redirect('login')
    

    #3
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required   

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm 


@login_required
def post_list(request):
    posts = Post.objects.all().order_by('-created_date')  # Order by most recent first
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post}) 


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
  # Don't save initially
            post.author = request.user  # Set author to current user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})

@login_required
def  post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:  # Check if user is the author
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)  # Update existing post
            if form.is_valid():
                form.save()
                return redirect('post_detail', pk=post.pk)
        else:
         return redirect('post_list')  # Redirect if not the author
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_update.html', {'form': form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:  # Check if user is the author
        post.delete()
    return redirect('post_list')