from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, user_profile
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
    path('register/', register, name='register'),
    path('profile/', user_profile, name='profile'),
    path("post/<int:pk>/delete/", "post/<int:pk>/update/", "post/new/")

]


from django.urls import path


urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('new/', views.PostCreateView.as_view(), name='post_create'),

    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(),name='post_delete'),

]