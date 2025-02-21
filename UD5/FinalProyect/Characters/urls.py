from django.urls import path # type: ignore
from . import views

app_name = 'characters'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('universes/', views.Universes.as_view(), name='universes'),
    path('characters/', views.CharacterList.as_view(), name='character_list'),
]