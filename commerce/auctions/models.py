from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    def __str__(self):
        return self.username


class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    class Categories(models.TextChoices):
        FASHION = "FAS", _("Fashion")
        TOYS = "TOY", _("Toys")
        ELE = "ELE", _("Electronics")
        HOME =  "HOM", _("Home")
        BOOKS = "BOK", _("Books")
        Others = "ETC", _("Others")
        UNKNOWN = "", _("No category listed")
    category = models.CharField(max_length=3, choices=Categories.choices, default="", blank=True)
    image = models.CharField(max_length=64, blank=True)
    watchlist = models.ManyToManyField(User, blank=True, related_name="watcher")
    creator = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="creator")
    closed = models.BooleanField(default=False)
    current_bidder = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="current_bid")

    def __str__(self):
        return f"{self.title}"


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidder")
    item = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    price = models.IntegerField()

    def __str__(self):
        return f"{self.user} : {self.price} on {self.item}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    item = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length=500)
    def __str__(self):
        return f"{self.user} : {self.comment}"
