from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import GameSession
import json

def home(request):
    return render(request, 'game/home.html')

def signup(request):
    return render(request, 'game/signup.html')

