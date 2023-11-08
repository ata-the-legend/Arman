from django.urls import path
from .views import ExportCategoryView, ExportPostView, ExportShortLinkView, ExportUserView


app_name = 'home'
urlpatterns = [
    path("export/category", ExportCategoryView.as_view(), name="export-category"),
    path("export/user", ExportUserView.as_view(), name="export-user"),
    path("export/post", ExportPostView.as_view(), name="export-post"),
    path("export/shortlink", ExportShortLinkView.as_view(), name="export-shortlink"),
]

