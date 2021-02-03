from rest_framework import serializers

from trip.api.serializers import TripSerializer
from user.models import UserTrip, User, DriverComment


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'phone',
            'name',
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'phone',
            'name',
            'lastname',
            'status'
        ]

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'phone',
            'password',
            'name',
            'lastname',
            'status',
        ]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }


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