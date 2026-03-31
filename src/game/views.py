
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import GameSession
import json

def signup(request):
    if request.method == 'POST':
        # Grab the JSON string sent from the hidden form field
        raw_data = request.POST.get('player_json_input')
        if raw_data:
            GameSession.objects.create(player_data=raw_data)
            return redirect('signup')

    return render(request, 'game/signup.html')

def home(request):
    return render(request, 'game/home.html')
