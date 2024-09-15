from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import UserProfileForm  # Import your custom form

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