from django.conf.urls import url
from django.urls import path, include
from user import views
from django.contrib import admin


urlpatterns = [
    path('login/', views.login),
    path('index/', views.index),
    path('register/', views.register),
    path('logout/', views.logout),
    path('profile/', views.profile),
    path('editProfile/', views.edit_profile),
    url(r'^active/(?P<active_code>.*)/$', views.ActiveUserView.as_view(), name="user_active"),
    # (?P<active_code# >.*)/$ extract the string and assign to active_code
]