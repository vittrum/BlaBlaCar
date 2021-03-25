from django.urls import path

from . import views

urlpatterns = [
    path('trips/<int:pk>/request/', views.UserTripRequestView.as_view()),
    path('trips/<int:pk>/withdraw/', views.UserWithdrawView.as_view()),
    path('cars/', views.UserGetCars.as_view()),
    path('trips/', views.UserGetTrips.as_view()),
]

