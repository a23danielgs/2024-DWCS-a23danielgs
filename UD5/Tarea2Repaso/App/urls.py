from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home.as_view(),name="home"),
    path('products/',views.ProductList.as_view(),name="listOfProducts"),
    path('products/favorito',views.AddFavoriteView.as_view(),name="favorito"),
    path('products/add',views.Añadir.as_view(),name="add"),
    path('products/<slug:slug>',views.ProductDetail.as_view(),name="detail"),
    path('products/<slug:slug>/update',views.Update.as_view(),name="update"),
    path('products/<slug:slug>/delete',views.Delete.as_view(),name="delete"),
]
