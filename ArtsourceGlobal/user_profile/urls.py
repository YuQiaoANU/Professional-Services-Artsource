from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('userDash/', views.view_profile, name='view_profile'),
    path('user_profile/userDash/upload_artwork', views.upload_artwork, name='upload_artwork')
]
