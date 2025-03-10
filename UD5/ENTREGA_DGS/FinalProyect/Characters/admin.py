from django.contrib import admin
from .models import Character,Universe

# Register your models here.

class CharacterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
    list_display = ("name","universe")
    list_filter = ["universe"]

class UniverseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
    list_display = ("name","date_of_creation","creator")
    list_filter = ["creator"]

admin.site.register(Character,CharacterAdmin)
admin.site.register(Universe,UniverseAdmin)