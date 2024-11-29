from django.urls import path # type: ignore
from . import views

app_name = 'characters'
urlpatterns = [
    path('<int:page>', views.all_characters, name='all_characters'),
#    path('<int:blog_id>/', views.detail, name='detail')
    path('detail/<int:character_id>',views.detail, name="detail"),
    path('search/',views.search,name="search"),
    path('universes',views.all_universes, name='all_universes'),
    path('universeDetail/<str:universe>',views.universe_detail,name='universe_detail')
]

