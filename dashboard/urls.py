from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = "dashboard"

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('profile', ProfilePage.as_view(), name="profile"),
    path('dev-api', DevAPIPage.as_view(), name="dev-api"),
    path('payment', PaymentPage.as_view(), name="payment"),
    path('settings', SettingsPage.as_view(), name="settings"),
]