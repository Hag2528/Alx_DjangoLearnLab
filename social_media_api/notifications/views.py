from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Notification

@login_required
def view_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
    for notification in notifications:
        notification.is_read = True
        notification.save()

    context = {'notifications': notifications}
    return render(request, 'notifications/list.html', context)