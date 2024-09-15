from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField
from .views import User
class CustomUserCreationForm(UserCreationForm):
    email = EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
#3
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
    def __init__(self, *args, **kwargs):

        user = kwargs.pop('user', None)
        super(PostForm, self).__init__(*args, **kwargs)
        if user:
            self.instance.author = user

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3:
            raise forms.ValidationError('Title must be at least 3 characters long.')
        return title 
