from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'role', 'sign_on']
    list_filter = ['role', 'sign_on']

admin.site.register(Review, ReviewAdmin)