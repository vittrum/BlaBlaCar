from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from user.forms import LoginForm
from user.models import User


class UserList(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'user/user_list.html', {'user_list': users})


def user_login(request):
    username = 'not authorized'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['phone']
    else:
        form = LoginForm()

    return render(request, 'user/user_login.html', {'form': form})


class UserLogin:
    pass
