from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "heading", "text", "published")
    list_filter = ("heading",)
    search_fields = ("heading", "text")
