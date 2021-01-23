from django.urls import path

from . import views
from .views import user_login

urlpatterns = [
    path('', views.UserList.as_view()),
    path('login/', user_login, name='login'),#views.UserLogin.as_view()),
]