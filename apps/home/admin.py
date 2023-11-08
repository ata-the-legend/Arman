from django.contrib import admin
from .models import Category, Post, ShortLink
from import_export.admin import ExportActionMixin

@admin.register(Category)
class CategoryAdmin(ExportActionMixin, admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(ShortLink)
class ShortLinkAdmin(admin.ModelAdmin):
    pass