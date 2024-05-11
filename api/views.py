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

def churn_risk(prob):
    return np.where(prob < 1/3, 'LowRisk',
            np.where(prob < 2/3, 'ModerateRisk',
            np.where(prob <= 1, 'HighRisk', np.nan)))

@api_view(['GET'])
def predict(request):
    # Load your model
    model_path = os.path.join(settings.BASE_DIR, 'api/model.pkl')
    with open(model_path, 'rb') as file:
        model = pickle.load(file)

    # Load the prepared data
    data_path = os.path.join(settings.BASE_DIR, 'api/churn_prepared.csv')
    result_3 = pd.read_csv(data_path)



    # Predict probabilities
    predprob = model.predict_proba(result_3.drop(['Churn', 'CustomerID'], axis=1))

    data = {
        'CustomerID': result_3.CustomerID,
        'Churn': result_3.Churn,
        'Tenure': result_3.Tenure,
        'PreferredLoginDevice': result_3.PreferredLoginDevice,
        'CityTier': result_3.CityTier,
        'WarehouseToHome': result_3.WarehouseToHome,
        'PreferredPaymentMode': result_3.PreferredPaymentMode,
        'Gender': result_3.Gender,
        'HourSpendOnApp': result_3.HourSpendOnApp,
        'NumberOfDeviceRegistered': result_3.NumberOfDeviceRegistered,
        'PreferedOrderCat': result_3.PreferedOrderCat,
        'SatisfactionScore': result_3.SatisfactionScore,
        'MaritalStatus': result_3.MaritalStatus,
        'NumberOfAddress': result_3.NumberOfAddress,
        'Complain': result_3.Complain,
        'OrderAmountHikeFromlastYear': result_3.OrderAmountHikeFromlastYear,
        'CouponUsed': result_3.CouponUsed,
        'OrderCount': result_3.OrderCount,
        'DaySinceLastOrder': result_3.DaySinceLastOrder,
        'CashbackAmount': result_3.CashbackAmount,
        'PredictedChurnRisk': churn_risk(predprob[:, 1]),
        'PredictedChurnProbability': predprob[:, 1],
        'CurrentDate': date.isoformat(date.today())
    }
    pred_addr_g = pd.DataFrame(data=data)
    pred_addr_g_sort = pred_addr_g.sort_values(by='PredictedChurnProbability', ascending=False)

    predictions = []

    for _, row in pred_addr_g_sort.iterrows():
        customer_prediction = CustomerPrediction(
            customer_id=row['CustomerID'],
            churn=row['Churn'],
            tenure=row['Tenure'],
            preferred_login_device=row['PreferredLoginDevice'],
            city_tier=row['CityTier'],
            warehouse_to_home=row['WarehouseToHome'],
            preferred_payment_mode=row['PreferredPaymentMode'],
            gender=row['Gender'],
            hour_spent_on_app=row['HourSpendOnApp'],
            number_of_device_registered=row['NumberOfDeviceRegistered'],
            prefered_order_cat=row['PreferedOrderCat'],
            satisfaction_score=row['SatisfactionScore'],
            marital_status=row['MaritalStatus'],
            number_of_address=row['NumberOfAddress'],
            complain=row['Complain'],
            order_amount_hike_from_last_year=row['OrderAmountHikeFromlastYear'],
            coupon_used=row['CouponUsed'],
            order_count=row['OrderCount'],
            day_since_last_order=row['DaySinceLastOrder'],
            cashback_amount=row['CashbackAmount'],
            predicted_churn_risk=row['PredictedChurnRisk'],
            predicted_churn_probability=row['PredictedChurnProbability'],
            current_date=row['CurrentDate']
        )
        customer_prediction.save()
        predictions.append(CustomerPredictionSerializer(customer_prediction).data)

    return Response(predictions, status=status.HTTP_200_OK)
