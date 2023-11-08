from django.contrib import admin
from .models import Category, Post, ShortLink

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(ShortLink)
class ShortLinkAdmin(admin.ModelAdmin):
    pass