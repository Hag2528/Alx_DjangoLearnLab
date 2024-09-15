from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, user_profile

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
    path('register/', register, name='register'),
    path('profile/', user_profile, name='profile'),
    path("post/<int:pk>/delete/", "post/<int:pk>/update/", "post/new/")

]