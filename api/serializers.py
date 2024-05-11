# api/serializers.py
from rest_framework import serializers
from .models import CustomerPrediction

class CustomerPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPrediction
        fields = '__all__'
