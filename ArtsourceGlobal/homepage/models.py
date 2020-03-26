# created by Vaanee 2018
# Data models which are used to define table schemas in the database are defined here.
from django.db import models
import datetime
from django.contrib.postgres.fields import ArrayField


# Date added, Is_booked (Boolean), Price, likes
# FK: Owner, Booking_data
#

class Business(models.Model):
    business_name = models.CharField(max_length=50)
    business_description = models.CharField(max_length=250)
    business_owner = models.ForeignKey('auth.User', related_name='business', on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business_name


class Artwork(models.Model):
    title = models.CharField(max_length=50)
    art_description = models.CharField(max_length=250)
    height = models.FloatField(default=0.0)
    width = models.FloatField(default=0.0)
    art_owner = models.ForeignKey('auth.User', related_name='artwork', on_delete=models.CASCADE)
    price_artwork_per_day = models.FloatField()
    likes = models.IntegerField(default=0)
    artwork_image = models.FileField(upload_to='artwork_images/%Y/%m/%d',
                                     default='static/homepage/artwork_images/no-img.jpeg')
    # booking_data = models.ForeignKey(Business, on_delete=models.CASCADE, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    # tags = ArrayField(models.CharField(max_length=200), blank=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    From_Date = models.DateField(auto_now=False, auto_now_add=False, default=datetime.date.today)
    To_Date = models.DateField(auto_now=False, auto_now_add=False)
    business_data = models.ForeignKey(Business, on_delete=models.CASCADE)
    artwork_data = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    total_price = models.FloatField(default=0.0)

    def __str__(self):
        return "Booking " + self.id + "date: " + '%Y%m%d'
