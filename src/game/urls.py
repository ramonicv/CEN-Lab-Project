from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('game_select/', views.game_select, name='game_select'),
    path('waterfall/', views.waterfall, name='waterfall'),
]

