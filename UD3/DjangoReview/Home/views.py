from django.shortcuts import render
from Characters.views import Character
import random

# Create your views here.

def home(request):
    randomCharacters = Character.objects.all()

    return render(request, 'Home/home.html')