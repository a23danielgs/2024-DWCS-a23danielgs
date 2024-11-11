from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html',)

def about(request):
    return render(request, 'generator/about.html',)

def password(request):

    thepassword = ''

    characters = list('abcdefghijklmnñopqrstuvwxyz')

    if (request.GET.get('uppercase')):
       mayus = list('')
       for x in characters:
        mayus+=x.upper()

       characters.extend('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')

    if (request.GET.get('numbers')):
       characters.extend('1234567890')

    if (request.GET.get('special')):
       characters.extend('+-*/¡¿?^Ç!$%&/()=:;_-')

    length = int(request.GET.get('length'))

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})