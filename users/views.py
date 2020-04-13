from django.shortcuts import get_object_or_404, redirect, render

from .forms import UserForm
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
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'user/form.html', {
                'form': form
            })
    else:
        form = UserForm()

        return render(request, 'user/form.html', {
            'form': form
        })
