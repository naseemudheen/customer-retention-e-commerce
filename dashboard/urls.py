from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = "dashboard"

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('profile', profile, name="profile"),
    path('dev-api', DevAPIPage.as_view(), name="dev-api"),
    path('payment', PaymentListPage.as_view(), name="payment"),
    path('settings', password_change_form, name="settings"),
]