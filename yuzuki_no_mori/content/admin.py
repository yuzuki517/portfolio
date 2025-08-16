# content/admin.py
from django.contrib import admin
from .models import Article, Tag

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "published_at", "updated_at")
    list_filter = ("status", "tags")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ("tags",)
    actions = ["publish", "unpublish"]

    @admin.action(description="Publish selected")
    def publish(self, request, queryset):
        queryset.update(status="PUBLISHED")

    @admin.action(description="Unpublish selected")
    def unpublish(self, request, queryset):
        queryset.update(status="DRAFT")

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)

