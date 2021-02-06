from django.urls import path

from . import views

urlpatterns = [
    path('car/add/', views.CarCreateView.as_view()),
    path('car/<int:pk>/', views.CarDeleteView.as_view()),
    path('trip/add/', views.TripCreateView.as_view()),
    path('', views.TripListView.as_view()),
    path('trip/<int:pk>/request/, ')
]