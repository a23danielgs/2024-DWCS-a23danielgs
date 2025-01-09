from django.shortcuts import render
from django.http import HttpResponse
from .models import course

# Create your views here.

def home(request):
    courses = course.objects.all()
    return render(request,'courses/home.html',{'courses':courses})