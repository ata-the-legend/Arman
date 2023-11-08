from rest_framework.viewsets import GenericViewSet, mixins, ModelViewSet
from .models import Post, Category
from .serializers import CategorySerializer, PostSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from .resources import CategoryResource, PostResource, ShortLinkResource, UserResource



class ExportCategoryView(APIView):

    def get(self, request):
        dataset = CategoryResource().export()
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="categories.csv"'
        return response
    

class ExportPostView(APIView):

    def get(self, request):
        dataset = PostResource().export()
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Posts.csv"'
        return response
    

class ExportShortLinkView(APIView):

    def get(self, request):
        dataset = ShortLinkResource().export()
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="ShortLinks.csv"'
        return response
    
class ExportUserView(APIView):

    def get(self, request):
        dataset = UserResource().export()
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Users.csv"'
        return response



class PostModelViewSet(ModelViewSet):

    serializer_class = PostSerializer
    queryset = Post.objects.all().select_related('publisher')


class CategoryModelViewSet(ModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.all().prefetch_related('posts')


    