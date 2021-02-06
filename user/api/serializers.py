from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from trip.api.serializers import TripSerializer
from user.models import UserTrip, User, DriverComment

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER



class UserLoginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        phone = data.get("phone", None)
        password = data.get("password", None)
        user = User.objects.get(phone=phone)  # authenticate(username=phone, password=password)

        if user is None or user.password != password:
            raise serializers.ValidationError(
                'A user with this phone and password is not found.'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given phone and password does not exists'
            )
        return {
            'phone': user.phone,
            'token': jwt_token
        }


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
    #trip = TripSerializer()
    #user = UserSerializer()

    class Meta:
        model = UserTrip
        fields = '__all__'


class DriverCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    driver = UserSerializer()

    class Meta:
        model = DriverComment
        fields = '__all__'
