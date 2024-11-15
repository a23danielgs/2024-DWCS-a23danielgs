from django.contrib import admin # type: ignore
from .models import Blog

admin.site.register(Blog)
