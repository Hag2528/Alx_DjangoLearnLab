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
from .models import User
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
    
  #Task 2 week 15
from django.contrib.auth.decorators import login_required  # OR 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import User
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
@login_required
def follow_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if user != request.user:
        request.user.following.add(user)
    return redirect('user_profile', user.username)  # Replace with your profile view url

@login_required
def unfollow_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    request.user.following.remove(user)
    return redirect('user_profile', user.username)
@login_required  # OR use a LoginRequiredMixin for class-based views
def my_view(request):
    # Your view logic using CustomUser.objects.all() or similar
    users = get_user_model().objects.all()  # Assuming CustomUser inherits from AbstractBaseUser
    # ... rest of your view logic
    return render(request, 'user.html', {'users': users})


class MyView(LoginRequiredMixin. View):  # Inherits from LoginRequiredMixin for authentication
    # Your view logic using CustomUser.objects.all() or similar
    def get(self, request):
        users = get_user_model().objects.all()  # Assuming CustomUser inherits from AbstractBaseUser
        # ... rest of your view logic
        return render(request, 'your_template.html', {'users': users})