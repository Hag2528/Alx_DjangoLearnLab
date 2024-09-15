from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, user_profile
from . import views

urlpatterns =[
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
    path('register/', register, name='register'),
    path('profile/', user_profile, name='profile'),
    path("post/<int:pk>/delete/", "post/<int:pk>/update/", "post/new/")

 
 ]
urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('new/', views.PostCreateView.as_view(), name='post_form'),

    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(),name='post_delete'),
    path('search/', views.search, name='search'),
    path('tags/<slug:tag_name>/', views.tag_detail, name='tag_detail'),
    # ... other URL patterns ...

]
urlpatterns = [
    path('tags/<slug:tag_slug>/', views.tag_posts, name='tag_posts'),
    path('search/', views.search, name='search'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('<int:post_id>/comments/new/', views.CommentCreateView, name='add_comment'),
    path('<int:comment_id>/edit/', views.CommentUpdateView, name='edit_comment'),
    path('<int:comment_id>/delete/', views.CommentDeleteView, name='delete_comment'),
]

