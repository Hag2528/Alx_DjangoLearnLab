from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import UserProfileForm  # Import your custom form
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm 
User = get_user_model()

def user_profile(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = UserProfileForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully!')
                return redirect('profile')
  # Redirect back to profile page
        else:
            form = UserProfileForm(instance=user)
        context = {'form': form}
        return render(request, 'accounts/profile.html', context)
    else:
        return redirect('login')
  #3 
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import  Post
from .forms import PostForm 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import stomUserCreationForm 
class PostListView(ListView):
    model = Post
    template_name = 'blog/templates/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/templates/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/templates/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/templates/post_edit.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/templates/post_confirm_delete.html'

    success_url = '/posts/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
 # Import your custom form


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']

            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
  # Redirect to your blog's home page
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request


from django.shortcuts import render
from django.db.models import Q
from .models import Post

def search(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |   
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        )
    else:
        posts = Post.objects.all()
    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})

from django.shortcuts import get_object_or_404
from .models import Post, Tag

def tag_posts(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tags__name=tag.name)
    return render(request, 'blog/tag_posts.html', {'tag': tag, 'posts': posts})