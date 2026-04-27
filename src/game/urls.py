from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('game_select/', views.game_select, name='game_select'),
    path('waterfall/', views.waterfall, name='waterfall'),
    path('fuck_the_dealer/', views.fuck_the_dealer, name='fuck_the_dealer'),
    path('kings_cup/', views.kings_cup, name='kings_cup'),
    path('ride_the_bus/', views.ride_the_bus, name='ride_the_bus'),
    path('flip_cup/', views.flip_cup, name='flip_cup'),
]

