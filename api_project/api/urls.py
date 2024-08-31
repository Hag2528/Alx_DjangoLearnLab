from django.contrib import admin
from django.urls import path
from .views import BookList
urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/',BookList.as_view()),
]