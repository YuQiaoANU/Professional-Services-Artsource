from django.db import models
from signup.models import UserProfile
from homepage.models import Artwork
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from datetime import date
#Create a Reservation Model which stores booking details
class Reservation(models.Model):
    booking_owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='bookingowner')
    art = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name='bookart')
    artist = models.ForeignKey(UserProfile,on_delete=models.CASCADE, related_name='artist')
    CheckIn = models.DateField()
    CheckOut = models.DateField()
    totalPrice = models.IntegerField(default = 0)

    def get_id(self):
        return self.id;
    def get_checkin(self):
        return self.CheckIn
    def get_checkout(self):
        return self.CheckOut



    class Meta:
        verbose_name_plural = 'Reservation'

    def __str__(self):
         return self.booking_owner
