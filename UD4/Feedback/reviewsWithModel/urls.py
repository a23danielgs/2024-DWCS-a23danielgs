from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.reviewWithModel),
    # path('thank_you',views.thank_you)
]