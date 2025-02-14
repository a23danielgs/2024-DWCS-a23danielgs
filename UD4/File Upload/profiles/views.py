from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from .models import UserProfile
from django.views.generic import ListView,DetailView,DeleteView

# Create your views here.


class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"

class ProfileView(ListView):
    template_name = "profiles/profile_list.html"
    model = UserProfile
    context_object_name = "profiles"

class DeleteStudentView(DeleteView):
    model = UserProfile
    success_url ="/profiles/list" 
    template_name = "profiles/profiles_delete.html"