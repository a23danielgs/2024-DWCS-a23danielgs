from django.shortcuts import render
from django.views import View
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.http import HttpResponseRedirect
from .models import Product
from .forms import ProductForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name = "App/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        favorite_slug = self.request.session.get("favorite_review")  
        if favorite_slug:
            favorite_product = get_object_or_404(Product, slug=favorite_slug)
            context["favorite_products"] = [favorite_product]  
        else:
            context["favorite_products"] = [] 
        return context

    
class ProductList(ListView):
    template_name = "App/list.html"
    model = Product
    context_object_name = "products"


class ProductDetail(DetailView):
    template_name = "App/detail.html"
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.slug)
        return context
    
class AddFavoriteView(View):
 def post(self, request):
    review_id = request.POST["review_id"]
    request.session["favorite_review"] = review_id
    return HttpResponseRedirect("/products/" + str(review_id))
 
class Añadir(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "App/add.html"
    success_url = "/products"

class Update(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "App/update.html"
    success_url = "/products"

class Delete(DeleteView):
    model = Product
    form_class = ProductForm
    template_name = "App/delete.html"
    success_url = "/products"