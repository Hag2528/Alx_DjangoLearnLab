from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField
from .views import User

from django import forms
from django.contrib.taggit.widgets import TagWidget


from crispy_forms import forms

from taggit.forms import TagWidget
class MyForm(forms.Form):
    tags = forms.CharField(required=False)
    # ... other fields

class MyForm(forms.Form):
    tags = forms.CharField(required=False)
    # ... other fields

    widgets = {
        'tags': TagWidget(),
        # ... other widget mappings
    }
class MyForm(forms.Form):
    tags = forms.CharField(required=False, widget=TagWidget())

    # ... other fields in your form

class CustomUserCreationForm(UserCreationForm):
    email = EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
#1
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User  # Import custom User model (if applicable)

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User  # Use custom User model (if applicable)
        fields = ('username', 'email', 'password1', 'password2')

# Add a crispy form helper (optional)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.layout = Layout(
        'username',
        'email',
        'password1', 
        'password2',
        Submit('Register', 'primary'),
    )
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
from .models import Comment  
class CommentForm(forms.ModelForm):
   class Meta: 
     model = Comment


from django import forms

class TagWidget(forms.TextInput):
    pass
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field 


class MyForm(forms.Form):
    tags = forms.CharField(required=False, label="Tags (separated by commas)")

    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('tags', css_class='form-control'),  # Add CSS class for styling
        )