from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register',views.register.as_view("LogoutView.as_view(template_name=", "LoginView.as_view(template_name="),
    path('logout/', views.logout, name='logout'),
    path('books/', views.list_books, name='book_list'),
    path('libraries/', views.LibraryDetailView.as_view(), name='library_detail'),
]


