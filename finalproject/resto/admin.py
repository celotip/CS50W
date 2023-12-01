from django.contrib import admin

from .models import Category, Item, User, Order

from django.contrib.auth.admin import UserAdmin

from django.db import models

# UserAdmin is needed to allow creation of users from the admin page with hashed passwords.
class MyUserAdmin(UserAdmin):
    model = User

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('table_no', "expiry")}),
    )

    list_display = ("id", "username", "table_no")

# ModelAdmin for order so that orders can be properly seen in the admin page
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "table", "get_items")

# Register your models here.
admin.site.register(User, MyUserAdmin)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Order, OrderAdmin)