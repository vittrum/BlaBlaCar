from django.urls import path

from . import views

urlpatterns = [
    path('add-car', views.add_car()),
]

