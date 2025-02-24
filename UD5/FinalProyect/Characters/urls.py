from django.urls import path # type: ignore
from . import views

app_name = 'characters'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('universes/', views.Universes.as_view(), name='universes'),
    path('characters/', views.CharacterList.as_view(), name='character_list'),
    path('character/<slug:slug>', views.CharacterDetail.as_view(), name='character_detail'),
    path('universes/<slug:slug>', views.UniverseDetail.as_view(), name='universe_detail'),
    path('edit/', views.SelectEdit, name='select_edit'),
    path('edit/edit/', views.Edit, name='edit'),
    path('add/',views.Add.as_view(),name="add"),
    path('update/',views.Update.as_view(),name="update"),
    path('delete/',views.Delete.as_view(),name="delete"),
    path('search/',views.search,name="search"),
]