from rest_framework import serializers
from apps.accounts.models import User
from apps.home.models import Post, Category

class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'phone', 'username']


class PostSerializer(serializers.ModelSerializer):
    publisher = UserListSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['update_at', 'create_at']

class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'status', 'publisher', 'update_at', 'create_at']
        read_only_fields = ['update_at', 'create_at']

class CategorySerializer(serializers.ModelSerializer):
    posts = PostListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'parent', 'posts']

