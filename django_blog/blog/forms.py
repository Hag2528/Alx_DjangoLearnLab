from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField

class CustomUserCreationForm(UserCreationForm):
    email = EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password')