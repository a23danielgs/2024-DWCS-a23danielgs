from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'form/home.html',)

def answers(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    city = request.GET.get('city')
    server = request.GET.get('server')
    rol = request.GET.get('rol')

    mail = ''
    if(request.GET.get('mail')):
        mail = 'Mail'

    payroll = ''
    if(request.GET.get('payroll')):
        payroll = 'Payroll'

    selfservice = ''
    if(request.GET.get('selfservice')):
        selfservice = 'Selfservice'

    datos = {
        "username": username,
        "password": password,
        "city":city,
        "server":server,
        "rol":rol,
        "mail":mail,
        "payroll":payroll,
        "selfservice":selfservice,
    }

    return render(request, 'form/answers.html', datos)