from django.urls import path

from . import views
from .views import login
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.UserList.as_view()),
    path('connect/', TemplateView.as_view(template_name='user/login.html')),
    path('login/', login, name='login'),#views.UserLogin.as_view()),
]

