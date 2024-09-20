from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('token/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
]