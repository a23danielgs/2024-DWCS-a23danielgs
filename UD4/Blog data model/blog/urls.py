from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.Index.as_view()),
    path('all_posts',views.PostsList.as_view(),name="all_posts"),
    path('<slug:slug>/',views.Detail.as_view(),name='detail'),
    path('read-later',views.ReadLater.as_view(),name='read_later')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)