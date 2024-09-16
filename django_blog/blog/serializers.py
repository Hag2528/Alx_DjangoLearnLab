from django import forms
from .models import Post, Tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']


    tags = forms.CharField(label='Tags')

    def clean_tags(self):
        tags_input = self.cleaned_data['tags']
        tags = [Tag.objects.get_or_create(name=tag.strip())[0] for tag in tags_input.split(',')]
        return tags
    
from django.forms import ModelForm
from .models import Post, Tag

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].widget.attrs['class'] = 'select2'

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows':4, 'cols': 50}),
        }



from django.contrib.auth.forms import UserCreationForm
from django import forms,User # for additional fields

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Add email field
    # Add other fields as needed

    class Meta:
        model = User  # Replace with your custom user model if applicable
        fields = ("username", "email", "password1", "password2")