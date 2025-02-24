from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Character,Universe
import random

# Create your views here.

class Home (ListView):
    template_name="Characters/home.html"
    model = Character
    context_object_name = "Characters"

    def get_queryset(self):
        Characters = list(Character.objects.all())
        return random.sample(Characters,3)
    
class Universes (ListView):
    template_name="Characters/universes.html"
    model = Universe
    context_object_name = "Universes"

class CharacterList (ListView):
    template_name="Characters/index.html"
    model = Character
    context_object_name = "Characters"

class CharacterDetail (DetailView):
    template_name = "Characters/character_detail.html"
    model = Character

class UniverseDetail (DetailView):
    template_name = "Characters/universe_detail.html"
    model = Universe