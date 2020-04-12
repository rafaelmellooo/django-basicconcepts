from django.shortcuts import render

from .models import User


def index(request):
    users = User.objects.all()
    return render(request, 'user/index.html', {
        'users': users
    })


def detail(request, id):
    user = User.objects.get(id=id)
    return render(request, 'user/detail.html', {
        'user': user
    })
