from rest_framework import generics, views, status
from rest_framework.response import Response

from user.models import User
from . import serializers as sr
from ..models import Car, City, CityTrip


class CarCreateView(views.APIView):
    def post(self, request):
        driver = User.objects.get(phone='2222')#self.request.user
        serializer = sr.CarCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        _validated = serializer.validated_data
        _validated['user'] = driver
        Car.objects.create(**_validated)
        return Response(status=status.HTTP_201_CREATED)


class CarDeleteView(generics.DestroyAPIView):
    serializer_class = sr.CarCreateSerializer
    queryset = Car.objects.all()


class TripCreateView(views.APIView):
    def post(self, request):
        _data = request.data
        out_city = City.objects.get(_data.pop("departure_city"))
        in_city = City.objects.get(_data.pop("destination_city"))
        trip_serializer = sr.TripSerializer()
        trip_serializer.is_valid(raise_exception=True)
        _validated = trip_serializer.validated_data
        _validated['departure_city'] = out_city
        _validated['destination_city'] = in_city
        CityTrip.objects.create(**_validated)
        return Response(status=status.HTTP_201_CREATED)


