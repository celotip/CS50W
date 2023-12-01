import json
import pytz
from datetime import datetime, timedelta, timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Category, Item, User, Order

# Create your views here.
# Check the time in KL timezone
def time():
    kuala_lumpur = pytz.timezone('Asia/Kuala_Lumpur')
    now = datetime.now()
    now_in_kuala_lumpur = now.astimezone(kuala_lumpur)
    nowtime = now_in_kuala_lumpur.time()
    return nowtime

@login_required
@csrf_exempt
def checkout_view(request):
    nowtime = time()
    expiry = request.user.expiry
    if nowtime > expiry:
        return render(request, "expired.html")
    return render(request, "checkout.html")

def expiry(request):
    return render(request, "expired.html")

@login_required
def extend(request, cat_id):
    nowtime = time()
    expiry = request.user.expiry
    if nowtime > expiry:
        return render(request, "expired.html")
    return render(request, "menu_ext.html", {
        "title": Category.objects.get(id=cat_id),
        "items": Item.objects.all().filter(category=cat_id),
        "time": request.user.expiry,
        "no": request.user.table_no,
    })

@login_required
def history(request):
    nowtime = time()
    expiry = request.user.expiry
    if nowtime > expiry:
        return render(request, "expired.html")
    orders = Order.objects.all().filter(table=request.user)
    total = 0
    for item in orders:
        item.items = json.loads(item.items)
        total += item.total
    return render(request, "history.html", {
        "orders": orders,
        "total": total,
    })

def index(request):
    return render(request, "index.html")

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
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

@login_required
def options(request, section_id):
    nowtime = time()
    expiry = request.user.expiry
    if nowtime > expiry:
        return render(request, "expired.html")
    return render(request, "item.html", {
        "items": Item.objects.all().filter(category=section_id)
    })

@login_required
def order(request):
    nowtime = time()
    expiry = request.user.expiry
    if nowtime > expiry:
        return render(request, "expired.html")
    else:
        exclude_list = ["Drinks", "Non-visible", "Kuah"]
        return render(request, "menu.html", {
            "categories": Category.objects.all().exclude(title__in=exclude_list),
            "no": request.user.table_no,
            "time": request.user.expiry
        })

@login_required
@csrf_exempt
def submit_checkout(request):
    nowtime = time()
    expiry = request.user.expiry
    if nowtime > expiry:
        return render(request, "expired.html")
    if request.method == "POST":
        data = json.loads(request.body)
        item_list = data.get("items", "")
        price = data.get("price", "")
        counter = data.get("counter", "")
        order = Order(
            table=request.user,
            total=price,
            items=json.dumps(item_list),
            counter=counter,
        )
        order.save()
        return JsonResponse({"message": "Order submitted"}, status=201)