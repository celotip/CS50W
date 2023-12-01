import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

from .models import User, Post, Follow, Status, Like


def index(request):
    return render(request, "network/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


@csrf_exempt
@login_required
def compose(request):

    # Composing a new post must be via POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    data = json.loads(request.body)

    # Create and save post model
    content = data.get("content", "")
    post = Post(
        user=request.user,
        content=content
    )
    post.save()

    return JsonResponse({"message": "Post successfully made."}, status=201)


def post(request, post_id):

    # Query for requested post
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)

    # Return post contents
    if request.method == "GET":
        return JsonResponse(post.serialize())
    else:
        return JsonResponse({
            "error": "GET or PUT request required."
        }, status=400)


def postview(request, page):
    posts = Post.objects.all().order_by("-timestamp")
    pall = Paginator(posts, 10)
    cur_page = pall.page(page).object_list
    return JsonResponse([post.serialize() for post in cur_page], safe=False)

@login_required
def profile(request):
    return render(request, "network/profile.html")

@csrf_exempt
def follow(request, user_id):
    if request.method == "PUT":
        following = User.objects.get(id=user_id)
        follow = Follow(follower=request.user, following=following)
        follow.save()
        return JsonResponse({"message": "User followed"}, status=201)

@csrf_exempt
def unfollow(request, user_id):
    if request.method == "PUT" or request.method == "GET":
        following = User.objects.get(id=user_id)
        follow = Follow.objects.get(follower=request.user, following=following)
        follow.delete()
        return JsonResponse({"message": "User unfollowed"}, status=201)

@login_required
def following(request, page):
    all_following = Follow.objects.all().filter(follower=request.user)
    following = [i.following for i in all_following]
    postsArr = []
    for follow in following:
        posts = Post.objects.all().filter(user=follow)
        for post in posts:
            postsArr.append(post)
    postsArr.sort(key=lambda x: x.timestamp, reverse=True)
    pall = Paginator(postsArr, 10)
    cur_page = pall.page(page).object_list
    return JsonResponse([post.serialize() for post in cur_page], safe=False)


def users(request):
    users = User.objects.all().exclude(username=request.user)
    return JsonResponse([user.serialize() for user in users], safe=False)

@login_required
def posts(request, page):
    posts = Post.objects.all().filter(user=request.user).order_by("-timestamp")
    pall = Paginator(posts, 10)
    cur_page = pall.page(page).object_list
    return JsonResponse([post.serialize() for post in cur_page], safe=False)

@login_required
def status(request, user_id):
    try:
        following = User.objects.get(id=user_id)
        test = Follow.objects.get(follower=request.user, following=following)
        status = Status(status=True)
        return JsonResponse(status.serialize(), safe=False)
    except Follow.DoesNotExist:
        status = Status()
        return JsonResponse(status.serialize(), safe=False)

@login_required
def count(request):
    followers = Follow.objects.filter(following=request.user).count()
    following = Follow.objects.filter(follower=request.user).count()
    return JsonResponse({"followers": followers, "following": following}, safe=False)

def following_page(request):
    return render(request, "network/following.html")

@csrf_exempt
def edit(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(pk=post_id)
        data = json.loads(request.body)
        post.content = data["content"]
        post.save()
        return JsonResponse({"message": "Post edited"}, status=201)

@csrf_exempt
def like(request, post_id):
    if request.method == "PUT":
        post = Post.objects.get(id=post_id)
        like = Like(user=request.user, post=post)
        like.save()
        return JsonResponse({"message": "Post liked"}, status=201)

@csrf_exempt
def unlike(request, post_id):
    if request.method == "PUT":
        post = Post.objects.get(id=post_id)
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        return JsonResponse({"message": "Post unliked"}, status=201)

@login_required
def likestatus(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        test = Like.objects.get(user=request.user, post=post)
        status = Status(status=True)
        return JsonResponse(status.serialize(), safe=False)
    except Like.DoesNotExist:
        status = Status()
        return JsonResponse(status.serialize(), safe=False)

def likecount(request, post_id):
    likes = Like.objects.filter(post=post_id).count()
    return JsonResponse({"likes": likes}, safe=False)

def countpall(request):
    posts = Post.objects.all().order_by("-timestamp")
    p = Paginator(posts, 10)
    cpall = p.num_pages
    return JsonResponse({"pages": cpall}, safe=False)

def countpfol(request):
    all_following = Follow.objects.all().filter(follower=request.user)
    following = [i.following for i in all_following]
    postsArr = []
    for follow in following:
        posts = Post.objects.all().filter(user=follow)
        for post in posts:
            postsArr.append(post)
    postsArr.sort(key=lambda x: x.timestamp, reverse=True)
    p = Paginator(postsArr, 10)
    cpfol = p.num_pages
    return JsonResponse({"pages": cpfol}, safe=False)

def countpprof(request):
    posts = Post.objects.all().filter(user=request.user)
    p = Paginator(posts, 10)
    cpprof = p.num_pages
    return JsonResponse({"pages": cpprof}, safe=False)
