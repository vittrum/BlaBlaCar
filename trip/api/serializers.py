from rest_framework import serializers

from trip.models import Car, City, Trip, TripComment, CityTrip
from user.models import UserTrip, User


class CarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        exclude = ['user']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'


class TripCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripComment
        fields = '__all__'


class CityTripSerializer(serializers.ModelSerializer):
    departure_city = CitySerializer()
    destination_city = CitySerializer()
    trip = TripSerializer()

    class Meta:
        model = CityTrip
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'phone',
            'name',
            'lastname',
            'status'
        ]


class TripRequestSerializer(serializers.ModelSerializer):
    trip = TripSerializer()
    user = UserSerializer()

    class Meta:
        model = UserTrip
        fields = '__all__'
