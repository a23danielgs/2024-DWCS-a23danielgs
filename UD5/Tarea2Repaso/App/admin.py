from django.contrib import admin
from .models import Category,Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}

admin.site.register(Category)
admin.site.register(Product,ProductAdmin)