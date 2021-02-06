from rest_framework import status, views, generics
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from BlaBlaCar import settings
from trip.models import Trip
from user.api.serializers import UserRegistrationSerializer, \
    UserLoginSerializer, UserTripSerializer
from user.models import User, UserTrip


class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)


class UserLoginView(ListAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        serializer.validate(request.data)
        _phone = serializer.data['phone']
        _token = serializer.data['token']
        _user = User.objects.get(phone=_phone)
        _role = _user.status
        settings.DB_LOGIN, settings.DB_PASS = settings.change_root(_role)
        print(settings.DB_LOGIN)
        return Response({'role': _role,
                         'token': _token,
                         'phone': _phone},
                        status=status.HTTP_200_OK)

    def get_queryset(self):
        return


class UserTripView(views.APIView):
    authentication_classes = [JSONWebTokenAuthentication, ]

    def post(self, request, pk):
        _data = request.data

        _user = self.request.user.id
        #_trip = Trip.objects.get(id=pk)
        _data['approved'] = False
        _data['user'] = _user
        _data['trip'] = pk

        user_trip_serializer = UserTripSerializer(data=_data)
        user_trip_serializer.is_valid(raise_exception=True)

        UserTrip.objects.create(**user_trip_serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)


class UserWithdrawView(generics.DestroyAPIView):
    authentication_classes = [JSONWebTokenAuthentication, ]
    serializer_class = UserTripSerializer
    queryset = UserTrip.objects.all()

