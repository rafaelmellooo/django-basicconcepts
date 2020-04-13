from django.shortcuts import get_object_or_404, render

from .models import User


def index(request):
    users = User.objects.all()
    return render(request, 'user/index.html', {
        'users': users
    })


def detail(request, slug):
    user = get_object_or_404(User, slug=slug)
    return render(request, 'user/detail.html', {
        'user': user
    })


def new(request):
    return render(request, 'user/new.html')
