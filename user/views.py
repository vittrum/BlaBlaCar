from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from user.forms import LoginForm
from user.models import User


class UserList(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'user/list.html', {'user_list': users})


def login(request):
    username = 'not authorized'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['phone']
    else:
        form = LoginForm()

    return render(request, 'user/logged_in.html', {'username': username})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create(form.cleaned_data)
            user.save()
            print(user)
        else:
            print('form not valid')
    else:
        form = RegisterForm()
    return 'user created'

