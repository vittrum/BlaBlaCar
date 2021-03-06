from django.urls import path

from . import views

urlpatterns = [
    path('trips/<int:pk>/request/', views.UserTripRequestView.as_view()),
    path('trips/<int:pk>/withdraw/', views.UserWithdrawView.as_view())
]

