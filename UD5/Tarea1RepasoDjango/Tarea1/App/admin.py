from django.contrib import admin
from .models import Degree,Student


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name_surname",)}
    list_filter = ("name_surname",)
    list_display = ("name_surname", "degree",)

admin.site.register(Student,StudentAdmin)
admin.site.register(Degree)
