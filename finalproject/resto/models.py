import json
from datetime import datetime, timedelta, time
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    expiry = models.TimeField()
    table_no = models.IntegerField(blank=True, default=1, choices=((i,i) for i in range(1, 11)))

    def save(self, *args, **kwargs):
        ex = datetime.now() + timedelta(minutes=30)
        extime = ex.time()
        if not self.id:
            self.expiry = extime
        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.table_no}"
        
class Category(models.Model):
    title = models.CharField(max_length=200)
    pic = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return f"{self.title}"

class Item(models.Model):
    title = models.CharField(max_length=200)
    pic = models.ImageField(null=True, blank=True, upload_to="images/")
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="options", default=1)

    def __str__(self):
        return f"{self.title}"

class Order(models.Model):
    items = models.CharField(max_length=200, blank=True)
    table = models.ForeignKey("User", on_delete=models.CASCADE, related_name="tableorder", null=True)
    total = models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=timezone.now)
    counter = models.IntegerField(default=1)

    def set_items(self, x):
        self.items = json.dumps(x)

    def get_items(self):
        order_list = []
        orders = json.loads(self.items)
        for order in orders:
            order_list.append(order["item"])
        return order_list