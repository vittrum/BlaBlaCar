from django.urls import path

from . import views

urlpatterns = [
    path('car/add/', views.CarCreateView.as_view()),
    path('car/<int:pk>/', views.CarDeleteView.as_view()),
    path('add/', views.TripCreateView.as_view()),
    path('', views.TripListView.as_view()),
    path('requests/<int:pk>/approve/', views.TripUserApproveView.as_view()),
    path('requests/<int:pk>/decline/', views.TripUserDeclineView.as_view()),
    path('<int:pk>/comments/add/', views.TripUserCommentAddView.as_view()),
    path('requests/', views.TripRequestsListView.as_view()),
    path('comments/', views.TripUserCommentListView.as_view()),
]