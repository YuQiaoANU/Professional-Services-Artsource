from django.urls import path, include
from user import views
from django.contrib import admin

app_name = 'user'

urlpatterns = [
    path('admin', admin.site.urls),
    path('login/', views.login),
    path('index/', views.index),
    path('register/', views.register),
    path('logout/', views.logout),

]