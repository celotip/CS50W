from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("categories", views.categories, name="categories"),
    path("category/<str:category_id>", views.category_function, name="category"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("<str:listing_id>/watch", views.watch, name="watch"),
    path("<str:listing_id>/listing", views.listing, name="listing"),
    path("<str:listing_id>/remove", views.remove, name="remove"),
    path("<str:listing_id>/bid", views.bid, name="bid"),
    path("<str:listing_id>/comment", views.comment, name="comment"),
    path("<str:listing_id>/close", views.close, name="close"),
]
