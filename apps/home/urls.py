from django.urls import path
from rest_framework import routers
from .views import ExportCategoryView, ExportPostView, ExportShortLinkView, ExportUserView ,\
    PostModelViewSet, CategoryModelViewSet


app_name = 'home'
urlpatterns = [
    path("export/category", ExportCategoryView.as_view(), name="export-category"),
    path("export/user", ExportUserView.as_view(), name="export-user"),
    path("export/post", ExportPostView.as_view(), name="export-post"),
    path("export/shortlink", ExportShortLinkView.as_view(), name="export-shortlink"),
]


router = routers.DefaultRouter()
router.register(prefix='posts' ,viewset=PostModelViewSet)
router.register(prefix='categories' ,viewset=CategoryModelViewSet)

urlpatterns += router.urls


