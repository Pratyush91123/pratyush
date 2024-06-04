from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('costumer_registration',costumer_registration,name='costumer_registration'),
]
