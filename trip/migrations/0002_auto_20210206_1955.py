# Generated by Django 3.1.6 on 2021-02-06 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trip', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='tripcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trip',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trip.car'),
        ),
        migrations.AddField(
            model_name='citytrip',
            name='departure_city',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='departure_city', to='trip.city'),
        ),
        migrations.AddField(
            model_name='citytrip',
            name='destination_city',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='destination_city', to='trip.city'),
        ),
        migrations.AddField(
            model_name='citytrip',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trip.trip'),
        ),
        migrations.AddField(
            model_name='car',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]