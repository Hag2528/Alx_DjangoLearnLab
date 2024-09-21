# from django.shortcuts import render

# # Create your views here.
# from rest_framework import generics, permissions
# from .models import User
# from rest_framework.authtoken.views import ObtainAuthToken
# from .serializers import UserSerializer

# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class LoginView(ObtainAuthToken):
#     pass


from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import authenticate, login
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class accountView(generics.GenericAPIView):
    permission_classes=[IsAuthenticated]
    queryset=User.objects.all()
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}) 


class ProfileView(APIView):
    def get(self, request):
        user = request.user  # Access authenticated user from request
        serializer = UserSerializer(user)
        return Response(serializer.data)
    