from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from .models import Character,Universe
from django.views import View
from django.views.generic.edit import CreateView,UpdateView,DeleteView 
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['from_character_list'] = True 
        return context

class CharacterDetail (DetailView):
    template_name = "Characters/character_detail.html"
    model = Character

class UniverseDetail (DetailView):
    template_name = "Characters/universe_detail.html"
    model = Universe

def search(request):
    query = request.GET.get('q','')

    fromUniverseDetail = request.GET.get('from_universe_detail','')

    charactersByName = Character.objects.filter(name__icontains=query) if query else Character.objects.all()
    charactersByUniverse = Character.objects.filter(universe__name__icontains=query) if query else Character.objects.all()
    Characters = charactersByName | charactersByUniverse

    if fromUniverseDetail:
        return render(request, 'Characters/index.html', {'Characters': Characters,'query':query,'from_universe_detail':fromUniverseDetail})
    return render(request, 'Characters/index.html', {'Characters': Characters,'query':query})

def SelectEdit (request):
    return render(request,'Characters/edit/select_edit.html')

def Edit(request):
    editingUniverse = request.GET.get('editUniverse', '').lower() == 'true'
    return render(request, 'Characters/edit/edit.html', {'editingUniverse': editingUniverse})

class Add (CreateView):
    template_name = "Characters/edit/add.html"
    success_url = "Characters/index.html"

    def get_context_data(self, **kwargs):
        model  =  self.request.GET.get('modelo','')
        form_class = self.request.GET.get('modeloFormulario','')
        return model,form_class

class Update (UpdateView):
    template_name = "students/student_update.html"
    model = Universe
    fields = [ 
        "name", 
        "degree"
    ] 
    success_url ="/students"

class Delete (DeleteView):
    model = Universe
    success_url ="/students" 
    template_name = "students/student_delete.html"