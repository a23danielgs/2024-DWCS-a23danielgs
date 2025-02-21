from django.shortcuts import render
from Characters.views import Character
import random

# Create your views here.

def home(request):
    Characters = list(Character.objects.all())
    Random_characters = random.sample(Characters, 3)

    return render(request, 'Home/home.html',{'characters':Random_characters})