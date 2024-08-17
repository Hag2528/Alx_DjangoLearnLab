from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register',views.register.as_view(), name='register'),
    path('logout/', views.logout, name='logout'),
    path('books/', views.list_books, name='book_list'),
    path('libraries/', views.LibraryDetailView.as_view(), name='library_detail'),
]