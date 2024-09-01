from django.contrib import admin
from django.urls import path
from .views import BookList
urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/',BookList.as_view()),
]


from rest_framework.routers import DefaultRouter
from .views import BookViewSet  # Assuming BookViewSet is in views.py

router = DefaultRouter()
router.register(prefix='books', viewset=BookViewSet)

urlpatterns = router.urls

