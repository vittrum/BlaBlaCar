from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view()),
    path('register/', views.UserRegistrationView.as_view()),
    path('trips/<int:pk>/request/', views.UserTripView.as_view()),
    path('trips/<int:pk>/withdraw/', views.UserWithdrawView.as_view())
]

