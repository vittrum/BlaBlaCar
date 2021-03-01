from rest_framework import generics, views, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from BlaBlaCar import settings
from user.api.serializers import UserSerializer
from user.models import User, UserTrip
from . import serializers as sr
from .serializers import TripSerializer
from ..models import Car, City, CityTrip, Trip, TripComment


class CarCreateView(views.APIView):
    # permission_classes = [IsAuthenticated, ]  # [AllowAny, ]IsAuthenticated,
    authentication_classes = [JSONWebTokenAuthentication, ]

    def post(self, request):
        driver = self.request.user
        serializer = sr.CarCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        _validated = serializer.validated_data
        _validated['user'] = driver
        Car.objects.create(**_validated)

        print(settings.DB_LOGIN)
        return Response(status=status.HTTP_201_CREATED)


class CarDeleteView(generics.DestroyAPIView):
    authentication_classes = [JSONWebTokenAuthentication, ]
    serializer_class = sr.CarCreateSerializer
    queryset = Car.objects.all()


class TripCreateView(views.APIView):
    authentication_classes = [JSONWebTokenAuthentication, ]

    def post(self, request):
        _data = request.data

        # Get id's from request JSON, get objects by id's
        out_city = City.objects.get(id=_data.pop("departure_city"))
        in_city = City.objects.get(id=_data.pop("destination_city"))
        # car = Car.objects.get(id=_data.pop('car'))

        # _data['car'] = car
        # Serialize trip by data left in request
        trip_serializer = sr.TripSerializer(data=_data)
        trip_serializer.is_valid(raise_exception=True)
        _validated = trip_serializer.validated_data

        # Create Trip
        _trip = Trip.objects.create(**_validated)

        # Create trip destination
        _validated['departure_city'] = out_city
        _validated['destination_city'] = in_city
        # Добрый день, Евгений Валерьевич

        CityTrip.objects.create(departure_city=out_city,
                                destination_city=in_city,
                                trip=_trip)

        return Response(status=status.HTTP_201_CREATED)


class TripListView(generics.ListAPIView):
    authentication_classes = [JSONWebTokenAuthentication, ]

    class Meta:
        model = Trip
        fields = '__all__'


class TripUserApproveView(views.APIView):
    authentication_classes = [JSONWebTokenAuthentication, ]

    def post(self, request, pk):
        _ut = UserTrip.objects.get(id=pk)
        _ut.acception = True
        _ut.save()

        return Response(status=status.HTTP_200_OK)


# Переделать на что-то типа None или Null, или сделать не bool,
# а статус, чтобы можно было отличить от ожидающих отклоненные
class TripUserDeclineView(views.APIView):
    authentication_classes = [JSONWebTokenAuthentication, ]

    def post(self, request, pk):
        _ut = UserTrip.objects.get(id=pk)
        _ut.acception = False
        _ut.save()

        return Response(status=status.HTTP_200_OK)


class TripRequestsListView(generics.ListAPIView):
    authentication_classes = [JSONWebTokenAuthentication, ]
    trip = TripSerializer
    user = UserSerializer

    class Meta:
        model = UserTrip
        fields = '__all__'


class TripUserCommentView(views.APIView):
    authentication_classes = [JSONWebTokenAuthentication, ]

    def post(self, request):
        _data = request.data
        _user = self.request.user
        _trip_id = _data['trip_id']
        _text = _data['text']
        _type = _data.get('type', 'comment')
        _trip = Trip.objects.get(id=_trip_id)
        TripComment.objects.create(
            text=_text,
            type=_type,
            trip=_trip,
            user=_user
        )
        return Response(status=status.HTTP_201_CREATED)
