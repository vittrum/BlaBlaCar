from rest_framework import generics, views, status
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from BlaBlaCar import settings
from user.models import UserTrip
from . import serializers as sr
from .serializers import TripSerializer, TripRequestSerializer, TripCommentSerializer
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
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    filterset_fields = ['status']
    search_fields = ['status', 'car__model_name']


class TripUserApproveView(views.APIView):
    authentication_classes = [JSONWebTokenAuthentication, ]

    def post(self, request, pk):
        _ut = UserTrip.objects.get(id=pk)
        _ut.acception = True
        _ut.save()

        return Response(status=status.HTTP_200_OK)


class TripUserDeclineView(views.APIView):
    authentication_classes = [JSONWebTokenAuthentication, ]

    def post(self, request, pk):
        _ut = UserTrip.objects.get(id=pk)
        _ut.acception = False
        _ut.save()

        return Response(status=status.HTTP_200_OK)


class TripRequestsListView(generics.ListAPIView):
    authentication_classes = [JSONWebTokenAuthentication, ]
    serializer_class = TripRequestSerializer

    class Meta:
        model = UserTrip
        fields = '__all__'

    def get_queryset(self):
        user = self.request.user
        return UserTrip.objects.filter(user=user)


class TripUserCommentAddView(views.APIView):
    authentication_classes = [JSONWebTokenAuthentication, ]

    def post(self, request, pk):
        _data = request.data
        _user = self.request.user
        _trip_id = pk
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


class TripUserCommentListView(generics.ListAPIView):
    authentication_classes = [JSONWebTokenAuthentication, ]
    serializer_class = TripCommentSerializer

    def get_queryset(self):
        queryset = TripComment.objects.all()
        filter_value = self.request.query_params.get('trip', None)
        if filter_value is not None:
            queryset = queryset.filter(id=filter_value)
        return queryset


