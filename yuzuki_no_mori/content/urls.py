# content/urls.py
from django.urls import path
from . import views

app_name = "content"
urlpatterns = [
    path("", views.list_view, name="list"),
    path("tag/<slug:slug>/", views.tag_view, name="tag"),
    path("<slug:slug>/", views.detail_view, name="detail"),
    path("<slug:slug>/preview/<str:token>/", views.preview_view, name="preview"),
]

