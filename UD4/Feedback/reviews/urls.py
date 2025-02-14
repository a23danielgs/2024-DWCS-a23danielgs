from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.review),
    # path('thank_you',views.thank_you)
]
