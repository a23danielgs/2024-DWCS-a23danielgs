from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from .models import Character,Universe
from .forms import CharacterForm,UniverseForm
from django.views import View
from django.views.generic.edit import CreateView,UpdateView,DeleteView 
import random
from django.apps import apps
from django.http import HttpResponseRedirect
from django.forms.models import modelform_factory
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

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
    Universes = Universe.objects.filter(name__icontains=query) if query else Character.objects.all()

    Characters = charactersByName | charactersByUniverse 

    if fromUniverseDetail:
        return render(request, 'Characters/index.html', {'Characters': Characters,'query':query,'from_universe_detail':fromUniverseDetail})
    return render(request, 'Characters/index.html', {'Characters': Characters,'Universes':Universes,'query':query})

def SelectEdit (request):
    return render(request,'Characters/edit/select_edit.html')

def Edit(request):
    editingUniverse = request.GET.get('editUniverse', '').lower() == 'true'
    return render(request, 'Characters/edit/edit.html', {'editingUniverse': editingUniverse})


# ADD

def get_model_by_name(model_name):
    models = {
        'Character': Character,
        'Universe':Universe
    }
    model = models.get(model_name)
    if model is None:
        raise ValueError(f"Modelo '{model_name}' no encontrado.")
    return model


class Add (CreateView):
    template_name = "Characters/edit/add.html"
    success_url = "/edit"

    def get_queryset(self):
        model_name = self.request.GET.get('modelo', 'Character')
        model = get_model_by_name(model_name)
        return model.objects.all()

    def get_form_class(self):
        form_class_name = self.request.GET.get('modeloFormulario', 'CharacterForm')
        return globals().get(form_class_name) 


# ADD
# UPDATE
class SelectUpdate(ListView):
    template_name = "Characters/edit/select_update.html"
    context_object_name = "Objects"
    
    def get_queryset(self):
        model_name = self.request.GET.get('modelo', 'Character')
        model = get_model_by_name(model_name)
        return model.objects.all()

    def get_form_class(self):
        form_class_name = self.request.GET.get('modeloFormulario', 'CharacterForm')
        return globals().get(form_class_name) 


def get_model_by_slug(slug):
    if Character.objects.filter(slug=slug).exists():
        return Character
    elif Universe.objects.filter(slug=slug).exists():
        return Universe

    else:
        raise ValueError(f"No se encontró ningún modelo para el slug '{slug}'")

class Update(UpdateView):
    template_name = "Characters/edit/update.html"
    success_url = "/edit"

    def get_model(self):
        slug = self.kwargs.get('slug')
        return get_model_by_slug(slug)

    def get_object(self, queryset=None):
        model = self.get_model()
        slug = self.kwargs.get('slug')
        return get_object_or_404(model, slug=slug)

    def get_form_class(self):
        model = self.get_model()
        return modelform_factory(model, exclude=["slug"])
# UPDATE
# DELETE

class SelectDelete(ListView):
    template_name = "Characters/edit/select_delete.html"
    context_object_name = "Objects"
    
    def get_queryset(self):
        model_name = self.request.GET.get('modelo', 'Character')
        model = get_model_by_name(model_name)
        return model.objects.all()

    def get_form_class(self):
        form_class_name = self.request.GET.get('modeloFormulario', 'CharacterForm')
        return globals().get(form_class_name) 
    
class Delete(DeleteView):
    template_name = 'Characters/edit/delete.html'
    success_url = "/edit"

    def get_model(self):
        slug = self.kwargs.get('slug')
        return get_model_by_slug(slug)
    
    def get_object(self, queryset=None):
        model = self.get_model()
        slug = self.kwargs.get('slug')
        return get_object_or_404(model, slug=slug)
    
    def get_form_class(self):
        model = self.get_model()
        return modelform_factory(model, exclude=["slug"])

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return redirect(self.success_url)

    
# DELETE

def agregar_favorito(request, character_slug):
    character = Character.objects.get(slug=character_slug)
    
    if 'favoritos' not in request.session:
            request.session['favoritos'] = []

    favoritos = request.session['favoritos']
       
    if character.slug in favoritos:
        favoritos.remove(character.slug)
    else:
        favoritos.append(character.slug)

    request.session['favoritos'] = favoritos  

    return redirect('characters:character_detail', slug=character_slug)

class VerFavoritos (ListView):
    model = Character
    template_name = 'Characters/favoritos.html' 
    context_object_name = 'favoritos'

    def get_queryset(self):
        favoritos_slug = self.request.session.get('favoritos', [])
        return Character.objects.filter(slug__in=favoritos_slug)