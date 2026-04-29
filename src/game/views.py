from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import GameSession

def home(request):
    return render(request, 'game/home.html')

def signup(request):
    return render(request, 'game/signup.html')

def game_select(request):
    return render(request, 'game/game_select.html')

def waterfall(request):
    return render(request, 'game/waterfall.html')

def screw_the_dealer(request):
    return render(request, 'game/screw_the_dealer.html')

def ride_the_bus(request):
    return render(request, 'game/ride_the_bus.html')