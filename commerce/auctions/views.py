from django import forms
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import User, Listing, Bid, Comment


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = 'title', 'description', 'price', 'category', 'image'


def bid(request, listing_id):
    if request.method == "POST":
        item = Listing.objects.get(pk=listing_id)
        bid = Bid(user=request.user, item=item, price=request.POST["bid"])
        item.price = request.POST["bid"]
        item.current_bidder = request.user
        item.save()
        bid.save()
        return HttpResponseRedirect(reverse("listing", args=(item.id,)))


def close(request, listing_id):
    if request.method == "POST":
        item = Listing.objects.get(pk=listing_id)
        item.closed = True
        item.save()
        return HttpResponseRedirect(reverse("listing", args=(item.id,)))


def comment(request, listing_id):
    if request.method == "POST":
        item = Listing.objects.get(pk=listing_id)
        comment = Comment(user=request.user, item=item, comment=request.POST["comment"])
        comment.save()
        return HttpResponseRedirect(reverse("listing", args=(item.id,)))



def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })


def watchlist(request):
    return render(request, "auctions/watchlist.html", {
        "listings": Listing.objects.all().filter(watchlist=request.user)
    })


def create(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            item = form.save()
            item.creator = request.user
            item.save()
            return HttpResponseRedirect(reverse("index"))
    form = ListingForm()
    return render(request, "auctions/create.html", {
        "form": form
    })


def categories(request):
    return render(request, "auctions/categorylist.html", {
        "categories": Listing.Categories.choices
    })


def category_function(request, category_id):
    return render(request, "auctions/category.html", {
        "listings": Listing.objects.all().filter(category=category_id),
        "category": Listing.Categories(category_id).label
    })


def watch(request, listing_id):
    if request.method == "POST":
        item = Listing.objects.get(pk=listing_id)
        watcher = request.user
        item.watchlist.add(watcher)
        return HttpResponseRedirect(reverse("listing", args=(item.id,)))


def remove(request, listing_id):
    if request.method == "POST":
        item = Listing.objects.get(pk=listing_id)
        watcher = request.user
        item.watchlist.remove(watcher)
        return HttpResponseRedirect(reverse("listing", args=(item.id,)))


@login_required(login_url = reverse_lazy("login"))
def listing(request, listing_id):
    item = Listing.objects.get(pk=listing_id)
    watcher = request.user
    return render(request, "auctions/listing.html", {
        "item": Listing.objects.get(pk=listing_id),
        "not_watchlist": Listing.objects.exclude(watchlist=watcher).all(),
        "category": Listing.Categories(item.category).label,
        "comments": item.comments.all()
    })


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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
