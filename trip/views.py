from django.shortcuts import render

# Create your views here.


def add_car(request):
    return render(request, 'driver/add_car.html')