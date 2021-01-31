from rest_framework import generics, views

from . import serializers as sr
from ..models import Car


class CarCreateView(views.APIView):
    def post(self, request):
        driver = self.request.user
        serializer = sr.CarCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        _validated = serializer.validated_data
        _validated['user'] = driver
        Car.objects.create(**_validated)


class CarDeleteView(generics.DestroyAPIView):
    serializer_class = sr.CarCreateSerializer
    queryset = Car.objects.all()


class TripCreateView(views.APIView):
    def post(self, request):
