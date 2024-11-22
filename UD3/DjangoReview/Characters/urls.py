from django.urls import path # type: ignore
from . import views

app_name = 'characters'
urlpatterns = [
    path('', views.all_characters, name='all_characters'),
#    path('<int:blog_id>/', views.detail, name='detail')
     path('<int:character_id>',views.detail, name="detail")
]

