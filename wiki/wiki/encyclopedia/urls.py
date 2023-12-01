from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entry, name="entry"),
    path("search/<str:search>", views.search, name="search"),
    path("new/page", views.new, name="new"),
    path("edit/<str:edit>", views.edit, name="edit"),
    path("random/page", views.random, name="random")
]
