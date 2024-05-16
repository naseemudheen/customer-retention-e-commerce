from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = "client"

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('docs', DocumentationView.as_view(), name="documentation"),
    path('contact-us', enquiryCreate.as_view(), name="enquiry_create"),

]