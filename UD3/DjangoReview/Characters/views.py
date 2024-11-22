from django.shortcuts import render, get_object_or_404
from .models import Character
# Create your views here.

def all_characters(request):
    characters = Character.objects.all()

    return render(request, 'Characters/allCharacters.html',{'characters':characters})

def detail(request, character_id):
    character = get_object_or_404(Character, pk=character_id)

    return render(request, 'Characters/detail.html',{'character':character})