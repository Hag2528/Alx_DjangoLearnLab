from django.shortcuts import render, redirect
from django.contrib.auth import login
from rest_framework  import generics
from .forms import CustomUserCreationForm 
class RegisterView(generics.CreateView):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
  # Replace 'home' with your desired redirect URL