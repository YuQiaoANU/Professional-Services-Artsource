import datetime
from django import forms
from django.shortcuts import render
from django.urls import reverse
from django.core.signing import Signer
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Q
from user.models import User
#from Authorize.models import UserRole
#from ManageHotels.models import Photo
from .models import Reservation
from django.shortcuts import render, redirect
from homepage.models import Artwork
from .forms import BookArtForm
from datetime import datetime

from django.views import View
from django.template.loader import get_template


## Generates a PDF using the render help function and outputs it as invoice.html




## Works out how long the user is staying in a hotel for also working out the total cost.
def bookArt(request, pk):
    artid = Artwork.objects.get(id=pk)
    if request.method == 'GET':
        form = BookArtForm()
        args = {'artid': artid, 'form':form,}
        return render(request, 'booking/bookart.html',args)
    else:
        form= BookArtForm(request.POST)
        if form.is_valid():
            checkin = form.cleaned_data['CheckIn']
            checkout = form.cleaned_data['CheckOut']
            delta = calc_delta(checkin,checkout)
            total_price_booking = calc_price(artid.price_artwork_per_day, delta.days)
            string_date = convert_to_str(delta)
            return render(request, 'booking/bookart.html', {'checkin':checkin,'checkout':checkout, 'artid':artid, 'delta':delta, 'total_price_booking':total_price_booking,'string_date':string_date})

def ReviewBooking(request,checkin,checkout, artid, delta, total_price):
      return render(request, 'finaliseBooking', {'checkin':checkin,'checkout':checkout, 'artid':artid, 'delta':delta, 'total_price_booking':total_price_booking,'string_date':string_date})


#'checkin':checkin,'checkout':checkout

def finaliseBooking(request, artid, checkin, checkout, totalcost):
    if request.method == 'POST':
        form = BookArtForm(request.POST)
        book = form.save(commit=False)
        book.user = request.user
        book.save()
        art = form.cleaned_data['artid']
        CheckIn = form.cleaned_data['checkin']
        CheckOut = form.cleaned_data['checkout']
        totalPrice = form.cleaned_data['totalcost']
        link = reverse('bookArt')
        return redirect(link)
        form = BookArtForm()
    return render(request, 'booking/review.html',{'form':form})




def calc_delta (checkin, checkout):
    date_format = "%Y-%m-%d"
    date1= datetime.strptime(str(checkin), date_format)
    date2=datetime.strptime(str(checkout), date_format)
    delta = date2 - date1
    return delta


def calc_price(price, delta):
    total_price = price*delta
    return total_price


def convert_to_str(delta):
    return str(delta)
# Stores the confirmed booking  into the database
def storeBooking(request,artid,checkin,checkout,totalcost):

    if request.method == 'POST':
        user = request.user
        art=Artwork.objects.get(artid)
        cost = totalcost
        newReservation = Reservation()
        newReservation.booking_owner = user
        newReservation.art = art
        newReservation.CheckIn = checkin
        newReservation.CheckOut = checkout
        newReservation.totalPrice = cost
        newReservation.save()
        #Deletes the session variables.
        del request.session['checkin']
        del request.session['checkout']
        link = reverse('homepage:view_profile')
        return HttpResponseRedirect(link)

    else:
        url = reverse('homepage:view_profile')
        return url
