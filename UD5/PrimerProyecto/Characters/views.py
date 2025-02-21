from django.shortcuts import render, get_object_or_404
from .models import Character
# Create your views here.

def all_characters(request, page):
    principio = 7*(page-1)
    final = page*7
    characters = Character.objects.all()[principio:final]
    return render(request, 'Characters/allCharacters.html',{'characters':characters})

def detail(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    return render(request, 'Characters/detail.html',{'character':character})

def search(request):
    query = request.GET.get('q','')

    charactersN = Character.objects.filter(name__icontains=query) if query else Character.objects.all()
    charactersD = Character.objects.filter(universe__icontains=query) if query else Character.objects.all()


    return render(request, 'Characters/search.html', {'charactersN': charactersN,'charactersD':charactersD, 'query': query})

def all_universes(request):
    queryset = Character.objects.all()
    dictionary = {obj.universe: obj for obj in queryset}

    return render(request, 'Characters/allUniverses.html',{'universes':dictionary})

def universe_detail(request, universe):
    characters = Character.objects.all()
    return render(request, 'Characters/universesDetail.html',{'characters':characters,'universe': universe})