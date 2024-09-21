from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('token/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
]

#Task 2 week 15

from django.urls import path
from . import views

urlpatterns = [
  path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
  path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow_user'),

  # ...
]

