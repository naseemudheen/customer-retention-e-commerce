from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = "client"

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
]