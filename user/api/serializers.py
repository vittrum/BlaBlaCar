from rest_framework import serializers

from trip.api.serializers import TripSerializer
from user.models import UserTrip, User, DriverComment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'phone',
            'name',
            'lastname',
            'status'
        ]


class UserTripSerializer(serializers.ModelSerializer):
    trip = TripSerializer()
    user = UserSerializer()

    class Meta:
        model = UserTrip
        fields = '__all__'


class DriverCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    driver = UserSerializer()

    class Meta:
        model = DriverComment
        fields = '__all__'