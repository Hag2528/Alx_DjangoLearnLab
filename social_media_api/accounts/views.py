from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import User
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(ObtainAuthToken):
    pass