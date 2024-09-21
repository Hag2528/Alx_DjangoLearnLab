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
    #task 2 week 15
        # from .models import User
        # from django.contrib.auth.decorators import login_required
        # from django.shortcuts import get_object_or_404
        # from django.http import HttpResponseRedirect

        # @login_required
        # def follow_user(request, user_id):
        #   user_to_follow = get_object_or_404(User, pk=user_id)
        #   request.user.following.add(user_to_follow)
        #   # Success message or redirect
        #   return HttpResponseRedirect('ghhhn')  # Replace with appropriate response

        # @login_required
        # def unfollow_user(request, user_id):
        #   user_to_unfollow = get_object_or_404(User, pk=user_id)
        #   request.user.following.remove(user_to_unfollow)
        #   # Success message or redirect
        #   return HttpResponseRedirect("ddd")  # Replace with appropriate response


from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import User
@login_required
def follow_user(request, user_id):
  user_to_follow = get_object_or_404(User, pk=user_id)
  if user_to_follow != request.user:  # Prevent self-follow
    request.user.follow(user_to_follow)
  return redirect('profile', user_id=user_id)  # Redirect after follow

@login_required
def unfollow_user(request, user_id):
  user_to_unfollow = get_object_or_404(User, pk=user_id)
  if user_to_unfollow != request.user:  # Prevent self-unfollow
    request.user.unfollow(user_to_unfollow)
  return redirect('profile', user_id=user_id)  # Redirect after unfollow



from django.shortcuts import render
from .models import Post, User

def get_feed(request):
  user = request.user
  following = user.following.all()
  posts = Post.objects.filter(author__in=following).order_by('-created_at')  # Get posts from followed users, order by creation date
  return render(request, 'feed.html', context={'posts': posts})




from django.contrib.auth.models import Permission

can_follow_permission = Permission.objects.get_or_create(codename='can_follow')
can_unfollow_permission = Permission.objects.get_or_create(codename='can_unfollow')