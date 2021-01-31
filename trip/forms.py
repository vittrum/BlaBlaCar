from django.forms import forms

from trip.models import Car


class CarForm(forms.ModelForm):
    model = Car
    fields = '__all__'