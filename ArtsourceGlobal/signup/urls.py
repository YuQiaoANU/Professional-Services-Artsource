from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url
from django.views.generic.base import TemplateView

from .views import signup

from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', TemplateView.as_view(template_name='homepage/index.html'), name='home'),

]
