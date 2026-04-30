from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('game_select/', views.game_select, name='game_select'),
    path('waterfall/', views.waterfall, name='waterfall'),
    path('screw_the_dealer/', views.screw_the_dealer, name='screw_the_dealer'),
    path('ride_the_bus/', views.ride_the_bus, name='ride_the_bus'),
    path('truth_or_drink/', views.truth_or_drink, name='truth_or_drink'),
    path('fsu_trivia/', views.fsu_trivia, name='fsu_trivia'),
]

