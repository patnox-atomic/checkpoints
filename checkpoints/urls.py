##Patnox 27-07-2021

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]