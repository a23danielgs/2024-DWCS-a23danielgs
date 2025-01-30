from django.contrib import admin
from .models import Tag,Author,Post

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display = ("title","date","Author")
    list_filter = ("Author","tag","date")


admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Post,PostAdmin)