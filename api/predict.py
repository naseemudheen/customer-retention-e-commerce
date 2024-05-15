import pickle
from django.conf import settings
from django.http import JsonResponse
import os
import numpy as np
import pandas as pd
from datetime import date

def churn_risk(prob):
    return np.where(prob<1/3,'LowRisk',
            np.where(prob<2/3, 'ModerateRisk',
            np.where(prob<=1, 'HighRisk', np.nan)))

def predict():
    # Load your model
    model_path = os.path.join(settings.BASE_DIR, 'api/churn_cust_model.pkl')
    with open(model_path, 'rb') as file:
        model = pickle.load(file)

    # Assume `data` is fetched from request
    data_path = os.path.join(settings.BASE_DIR, 'api/churn_prepered.csv')
    result_3 = pd.read_csv(data_path)

    predprob =model.predict_proba(result_3.drop(['Churn', 'CustomerID'], axis = 1))
    pd.DataFrame(predprob).shape
    result_data = pd.concat([result_3[['CustomerID']].reset_index(drop=True),
                            pd.DataFrame(predprob[:,1], columns=['PredictedChurnProbability'])],
                            axis=1)
    #functiontoclassifyriskbasedonprobability

    # prediction = model.predict([data])

    #W/Googlename
    #Colsforchartresult_r2B.columns﴿﴿#AptName_ys
    data = {'CustomerID' :result_3.CustomerID,
            'Tenure': result_3.Tenure,
            'DaySinceLastOrder':result_3.DaySinceLastOrder,
            'CashbackAmount':result_3.CashbackAmount,
            'DaySinceLastOrder':result_3.DaySinceLastOrder, #result_r2
            'PredictedChurnRisk': churn_risk(predprob[:,1]),
            'PredictedChurnProbability':predprob[:,1],
            'CurrentDate':date.isoformat(date.today())
        }
    pred_addr_g=pd.DataFrame(data=data)
    #pred_addr_g['District']=pred_addr_g['District'].fillna﴾''﴿
    pred_addr_g_sort = pred_addr_g.sort_values(by='PredictedChurnProbability',ascending=False)
    print(pred_addr_g_sort.head())
    #forinternaluse
    return "hello world"






