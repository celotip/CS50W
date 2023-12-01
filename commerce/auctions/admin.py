from django.contrib import admin

from .models import User, Listing, Bid, Comment

# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "category")
    filter_horizontal = ("watchlist",)

admin.site.register(User)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Bid)
admin.site.register(Comment)
