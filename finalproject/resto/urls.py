from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("order", views.order, name="order"),
    path("order/<int:cat_id>", views.extend, name="extend"),
    path("accounts/login/", views.login_view, name="login"),
    path("checkout", views.checkout_view, name="checkout"),
    path("order/options/<int:section_id>", views.options, name="options"),
    path("checkout/submit", views.submit_checkout, name="submit_checkout"),
    path("history", views.history, name="history"),
    path("account_expired", views.expiry, name="account_expired"),
    path("logout", views.logout_view, name="logout"),
]
