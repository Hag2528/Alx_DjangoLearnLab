from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('posts',views.PostViewSet) 

router.register('posts/(?P<pk>\d+)/comments', views.CommentViewSet, basename='comments')  # Nested routing

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/like/', views.like_post, name='like_post'),
    path('<int:pk>/unlike/', views.unlike_post, name='unlike_post'),
]
urlpatterns = [
  path('feed/', views.get_feed, name='feed'),
  # ...
]
