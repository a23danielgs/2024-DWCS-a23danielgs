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
    path('update/',views.SelectUpdate.as_view(),name="update"),
    path('update/<slug:slug>/',views.Update.as_view(),name="SelectedUpdate"),
    path('delete/',views.SelectDelete.as_view(),name="delete"),
    path('delete/<slug:slug>/',views.Delete.as_view(),name="SelectdDelete"),
    path('search/',views.search,name="search"),
    path('agregar_favorito/<slug:character_slug>/', views.agregar_favorito, name='agregar_favorito'),
    path('favoritos/', views.VerFavoritos.as_view(), name='favoritos'),

]