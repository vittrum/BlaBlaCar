from django.db import models


class Car(models.Model):
    baggage_volume = models.IntegerField(blank=True)
    status = models.CharField(default='car_status', max_length=50)
    mark = models.CharField(max_length=50)
    model_name = models.CharField(max_length=30)
    places_count = models.IntegerField()
    # top_list_driver = ?
    # top_list_driver = ?

    user = models.ForeignKey('user.User', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.mark} {self.model_name}'

    class Meta:
        db_table = 'cars'


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cities'


class Trip(models.Model):
    address = models.CharField(max_length=100)
    departure_date = models.DateField(blank=True)
    departure_time = models.TimeField(blank=True)
    places_available = models.IntegerField(blank=True)
    status = models.CharField(max_length=100, default='trip_status')

    # user_id - foreign key?

    def __str__(self):
        return self.address

    class Meta:
        db_table = 'trips'


class TripComment(models.Model):
    text = models.CharField(max_length=500)
    type = models.CharField(max_length=30, default='comment')

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'trips_comments'


class CityTrip(models.Model):
    departure_city = models.ForeignKey(City, on_delete=models.CASCADE,
                                       related_name='departure_city', blank=True)
    destination_city = models.ForeignKey(City, on_delete=models.CASCADE,
                                         related_name='destination_city', blank=True)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'trips_cities'
