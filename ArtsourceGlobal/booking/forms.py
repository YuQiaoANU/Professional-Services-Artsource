from .models import Reservation
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class BookArtForm(forms.ModelForm):
    class Meta:
        model = Reservation
        field = ('CheckIn', 'CheckOut',)
        exclude = ('booking_owner', 'art', 'artist', 'totalPrice',)
        widgets = {
            'CheckIn': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            'CheckOut': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
        }

