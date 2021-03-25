from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

import trip.models


class UserManager(BaseUserManager):
    def create_user(self, phone, name, lastname, password=None):
        if not phone:
            raise ValueError('Phone number required!')

        user = self.model(
            phone=phone,
            name=name,
            lastname=lastname
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(phone=phone, password=password,
                                name='superuser', lastname='superuser')
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    status = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.phone

    class Meta:
        db_table = "user"


class UserTrip(models.Model):
    acception = models.CharField(max_length=50, default=None,
                                 blank=True, null=True)
    trip = models.ForeignKey(trip.models.Trip, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.acception

    class Meta:
        db_table = 'users_trips'


class DriverComment(models.Model):
    text = models.CharField(max_length=500)
    type = models.CharField(max_length=30, default='driver_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client')
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='driver')

    # Евгений Валерьевич, а вы точно весь код смотрите?
    def __str__(self):
        return self.text

    class Meta:
        db_table = 'drivers_comments'
