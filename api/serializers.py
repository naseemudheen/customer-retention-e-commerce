# api/serializers.py
from rest_framework import serializers
from .models import CustomerPrediction


class CustomerPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPrediction
        fields = [
            "customer_id",
            "tenure",
            "preferred_login_device",
            "city_tier",
            "warehouse_to_home",
            "preferred_payment_mode",
            "gender",
            "hour_spent_on_app",
            "number_of_device_registered",
            "prefered_order_cat",
            "satisfaction_score",
            "marital_status",
            "number_of_address",
            "complain",
            "order_amount_hike_from_last_year",
            "coupon_used",
            "order_count",
            "day_since_last_order",
            "cashback_amount",
            "predicted_churn_risk",
            "predicted_churn_probability",
            "current_date",
            "created_at",
        ]
        read_only_fields = [
            "predicted_churn_risk",
            "predicted_churn_probability",
            "current_date",
            "created_at",
        ]
        extra_kwargs = {
            'preferred_login_device': {'write_only': True,},
            'city_tier': {'write_only': True,},
            'warehouse_to_home': {'write_only': True,},
            'preferred_payment_mode': {'write_only': True,},
            'gender': {'write_only': True,},
            'hour_spent_on_app': {'write_only': True,},
            'number_of_device_registered': {'write_only': True,},
            'prefered_order_cat': {'write_only': True,},
            'satisfaction_score': {'write_only': True,},
            'marital_status': {'write_only': True,},
            'number_of_address': {'write_only': True,},
            'complain': {'write_only': True,},
            'order_amount_hike_from_last_year': {'write_only': True,},
            'coupon_used': {'write_only': True,},
            'order_count': {'write_only': True,},
        }