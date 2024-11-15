from django.urls import path # type: ignore
from . import views


urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail')
]