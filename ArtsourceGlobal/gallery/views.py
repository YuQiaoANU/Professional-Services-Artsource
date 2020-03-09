from django.shortcuts import render
from django.http import HttpResponse
from homepage.models import Artwork

def index(request):
    artwork = Artwork.objects.all()
    return render(request, 'gallery/index.html', {'artwork':artwork})

def artwork_detail(request,pk):
    artid = Artwork.objects.get(id=pk)
    return render(request, './artworkpage/index.html', {'artid': artid})
