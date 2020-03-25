from django.urls import path, include
from terms import views
from django.contrib import admin

app_name = 'terms'

urlpatterns = [
    path('terms1/', views.terms1),

]