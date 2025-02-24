from django.contrib import admin
from .models import Character,Universe

# Register your models here.

class CharacterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}

class UniverseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}

admin.site.register(Character,CharacterAdmin)
admin.site.register(Universe,UniverseAdmin)