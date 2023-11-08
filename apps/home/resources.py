from import_export import resources
from apps.accounts.models import User
from .models import Category, Post, ShortLink

class CategoryResource(resources.ModelResource):

    class Meta:
        model = Category

class PostResource(resources.ModelResource):

    class Meta:
        model = Post


class ShortLinkResource(resources.ModelResource):

    class Meta:
        model = ShortLink


class UserResource(resources.ModelResource):

    class Meta:
        model = User

        