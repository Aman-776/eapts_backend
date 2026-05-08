# person/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_api, name="login"),
    path("logout/", views.logout_api, name="logout"),
    path("csrf/", views.get_csrf, name="csrf"),
]
