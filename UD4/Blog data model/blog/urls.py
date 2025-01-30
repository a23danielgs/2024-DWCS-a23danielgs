from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.index),
    path('all_posts',views.all_posts,name="all_posts"),
    path('<slug:slug>/',views.detail,name='detail')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)