from django.urls import path
from .views import *

app_name = "api"

urlpatterns = [
    path('predict/', PredictView.as_view(), name="predict"),
    path('bulk-predict/', BulkPredictView.as_view(), name="predict"),

 
]