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
