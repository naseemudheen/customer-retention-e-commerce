from django.shortcuts import render

# Create your views here.
# api/views.py
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import os
import pickle
import numpy as np
import pandas as pd
from datetime import date
from .models import CustomerPrediction
from .serializers import CustomerPredictionSerializer
from rest_framework.views import APIView

# loading the model
model_path = os.path.join(settings.BASE_DIR, "api/churn_cust_model.pkl")
with open(model_path, "rb") as file:
    model = pickle.load(file)

def churn_risk(prob):
    return np.where(
        prob < 1 / 3,
        "LowRisk",
        np.where(prob < 2 / 3, "ModerateRisk", np.where(prob <= 1, "HighRisk", np.nan)),
    )


def transform_data(data):
    return {
        "Tenure": [data["tenure"]],
        "CityTier": [data["city_tier"]],
        "WarehouseToHome": [data["warehouse_to_home"]],
        "HourSpendOnApp": [data["hour_spent_on_app"]],
        "NumberOfDeviceRegistered": [data["number_of_device_registered"]],
        "SatisfactionScore": [data["satisfaction_score"]],
        "NumberOfAddress": [data["number_of_address"]],
        "Complain": [data["complain"]],
        "OrderAmountHikeFromlastYear": [data["order_amount_hike_from_last_year"]],
        "CouponUsed": [data["coupon_used"]],
        "OrderCount": [data["order_count"]],
        "DaySinceLastOrder": [data["day_since_last_order"]],
        "CashbackAmount": [data["cashback_amount"]],
        "PreferredLoginDevice_Computer": [
            1 if data["preferred_login_device"] == "Computer" else 0
        ],
        "PreferredLoginDevice_Mobile": [
            1 if data["preferred_login_device"] == "Mobile" else 0
        ],
        "PreferredPaymentMode_COD": [
            1 if data["preferred_payment_mode"] == "COD" else 0
        ],
        "PreferredPaymentMode_Credit Card": [
            1 if data["preferred_payment_mode"] == "Credit Card" else 0
        ],
        "PreferredPaymentMode_Debit Card": [
            1 if data["preferred_payment_mode"] == "Debit Card" else 0
        ],
        "PreferredPaymentMode_E wallet": [
            1 if data["preferred_payment_mode"] == "E wallet" else 0
        ],
        "PreferredPaymentMode_UPI": [
            1 if data["preferred_payment_mode"] == "UPI" else 0
        ],
        "Gender_Female": [1 if data["gender"] == "Female" else 0],
        "Gender_Male": [1 if data["gender"] == "Male" else 0],
        "PreferedOrderCat_Fashion": [
            1 if data["prefered_order_cat"] == "Fashion" else 0
        ],
        "PreferedOrderCat_Grocery": [
            1 if data["prefered_order_cat"] == "Grocery" else 0
        ],
        "PreferedOrderCat_Laptop & Accessory": [
            1 if data["prefered_order_cat"] == "Laptop & Accessory" else 0
        ],
        "PreferedOrderCat_Mobile": [1 if data["prefered_order_cat"] == "Mobile" else 0],
        "PreferedOrderCat_Others": [1 if data["prefered_order_cat"] == "Others" else 0],
        "MaritalStatus_Divorced": [1 if data["marital_status"] == "Divorced" else 0],
        "MaritalStatus_Married": [1 if data["marital_status"] == "Married" else 0],
        "MaritalStatus_Single": [1 if data["marital_status"] == "Single" else 0],
    }


class PredictView(APIView):
    def post(self, request):
        serializer = CustomerPredictionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        customer_prediction = serializer.save(
            current_date=date.isoformat(date.today()), user=request.user
        )
        model_input = transform_data(request.data)

        # Convert dictionary to DataFrame
        model_input_df = pd.DataFrame(model_input)
        predprob = model.predict_proba(model_input_df)

        customer_prediction.predicted_churn_risk = churn_risk(predprob[0, 1])
        customer_prediction.predicted_churn_probability = predprob[0, 1]
        customer_prediction.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class BulkPredictView(APIView):
    def post(self, request):
        for data in request.data:
            serializer = CustomerPredictionSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            customer_prediction = serializer.save(
                current_date=date.isoformat(date.today()), user=request.user
            )
            model_input = transform_data(data)

            # Convert dictionary to DataFrame
            model_input_df = pd.DataFrame(model_input)
            predprob = model.predict_proba(model_input_df)

            customer_prediction.predicted_churn_risk = churn_risk(predprob[0, 1])
            customer_prediction.predicted_churn_probability = predprob[0, 1]
            customer_prediction.save()
        return Response(serializer.data, status=status.HTTP_200_OK)