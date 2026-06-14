from django.contrib import admin
from .models import SiteSetting, Page, BlogPost, FAQ


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ("site_name",)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "is_homepage", "is_published", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("is_homepage", "is_published")
    search_fields = ("title", "content", "meta_title", "meta_description")


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "is_published", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("is_published",)
    search_fields = ("title", "content", "meta_title", "meta_description")


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "is_active")
    list_filter = ("is_active",)