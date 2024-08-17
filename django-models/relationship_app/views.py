from django.shortcuts import render , redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm

def register(request):
     form=UserCreationForm(request.Post)
     if form.is_valid():
          form.save()
          return redirect("login")


# Create your views here.
