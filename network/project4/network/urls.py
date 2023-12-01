
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("posts/compose", views.compose, name="compose"),
    path("posts/<int:post_id>", views.post, name="post"),
    path("posts/page/<int:page>", views.postview, name="postview"),
    path("profile", views.profile, name="profile"),
    path("following", views.following_page, name="following_page"),
    path("posts/following/page/<int:page>", views.following, name="following"),
    path("<int:user_id>/status", views.status, name="status"),
    path("<int:user_id>/follow", views.follow, name="follow"),
    path("<int:user_id>/unfollow", views.unfollow, name="unfollow"),
    path("profile/users", views.users, name="users"),
    path("profile/posts/page/<int:page>", views.posts, name="posts"),
    path("profile/count", views.count, name="count"),
    path("<int:post_id>/edit", views.edit, name="edit"),
    path("<int:post_id>/like", views.like, name="like"),
    path("<int:post_id>/unlike", views.unlike, name="unlike"),
    path("<int:post_id>/likestatus", views.likestatus, name="likestatus"),
    path("<int:post_id>/likecount", views.likecount, name="likecount"),
    path("countpage/all", views.countpall, name="countpall"),
    path("countpage/following", views.countpfol, name="countpfol"),
    path("countpage/profile", views.countpprof, name="countpprof"),
]
