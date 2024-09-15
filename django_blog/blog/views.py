# Create your views here.
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Custom User model (optional, for additional profile fields)
# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#     # Add your custom fields here (e.g., profile_picture, bio)
#     pass

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:home')   
  # Replace 'blog:home' with your actual home URL pattern
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.GET:
                return redirect(request.GET['next'])  # Redirect to requested URL if provided
            return redirect('blog:home')  # Replace 'blog:home' with your actual home URL pattern
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'registration/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('blog:home')  # Replace 'blog:home' with your actual home URL pattern

def profile(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = PasswordChangeForm(user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request,user)  # Maintain session after password change
                messages.success(request, 'Your password has been changed successfully!')
        else:
            form = PasswordChangeForm(user)
        context = {'form': form}
        return render(request, 'registration/profile.html', context)
    else:
        return redirect('login')