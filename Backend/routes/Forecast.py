import pickle, json
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from connection import collection3, data

import numpy as np
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.ensemble import IsolationForest

ForecastRoute = APIRouter()

with open('models/Sales.pkl','rb') as file:
  model1 = pickle.load(file)
with open('models/Profit.pkl','rb') as file:
  model2 = pickle.load(file)

# Forecast Defintions
def forecastModelSales(steps=12):
    # Selecting the specific columns you want
    selected_columns = ['sales','day', 'month', 'year']

    # Creating a new DataFrame 'dataSales'
    dataSales = data[selected_columns]

    # Grouping the data by 'year' and 'month' and summing up the values
    msp = dataSales.groupby(['year', 'month']).agg({'sales': 'sum'}).reset_index()
    df = pd.DataFrame(msp)

    # Fit a SARIMA model
    order = (1, 1, 1)  # (p, d, q)
    seasonal_order = (1, 1, 1, 12)  # (P, D, Q, S)
    model1 = SARIMAX(df['sales'], order=order, seasonal_order=seasonal_order)
    results1 = model1.fit()

    forecast_steps = steps
    forecast = results1.get_forecast(steps=forecast_steps)
    forecast_index = np.arange(len(df['sales']) + 1, len(df['sales']) + 1 + forecast_steps)

    # Create a new DataFrame with past months values
    past_values = df['sales']

    # Create a new DataFrame with forecast.predicted_mean values
    forecast_values = forecast.predicted_mean

    # Concatenate the past values and forecast values into a single DataFrame
    fullSet = pd.concat([past_values, forecast_values], axis=0)

    # Send the predictions to MongoDB
    try:
        collection3.delete_many({"forecastSales": {"$exists": True}})
        collection3.insert_one({"forecastSales": fullSet.to_json()})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.','data': fullSet}

def forecastModelProfit(steps=12):
    # Selecting the specific columns you want
    selected_columns = ['profit','day', 'month', 'year']

    # Creating a new DataFrame 'dataSales'
    dataSales = data[selected_columns]

    # Grouping the data by 'year' and 'month' and summing up the values
    msp = dataSales.groupby(['year', 'month']).agg({'profit': 'sum'}).reset_index()
    df = pd.DataFrame(msp)

    # Fit a SARIMA model
    order = (1, 1, 1)  # (p, d, q)
    seasonal_order = (1, 1, 1, 12)  # (P, D, Q, S)
    model1 = SARIMAX(df['profit'], order=order, seasonal_order=seasonal_order)
    results1 = model1.fit()

    forecast_steps = steps
    forecast = results1.get_forecast(steps=forecast_steps)
    forecast_index = np.arange(len(df['profit']) + 1, len(df['profit']) + 1 + forecast_steps)

    # Create a new DataFrame with past months values
    past_values = df['profit']

    # Create a new DataFrame with forecast.predicted_mean values
    forecast_values = forecast.predicted_mean

    # Concatenate the past values and forecast values into a single DataFrame
    fullSet = pd.concat([past_values, forecast_values], axis=0)

    # Send the predictions to MongoDB
    try:
        collection3.delete_many({"forecastProfit": {"$exists": True}})
        collection3.insert_one({"forecastProfit": fullSet.to_json()})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.','data': fullSet}

# Forecast Routes

@ForecastRoute.post('/forecastSales')
async def forecast_route():
    return forecastModelSales()

@ForecastRoute.post('/forecastProfit')
async def forecast_profit_route():
    return forecastModelProfit()


# Frontend Forecast

@ForecastRoute.get('/GetForecastSales')
def get_forecast_route(step:int):
    try:
        docs = collection3.find()
        for doc in docs:
            if 'forecastSales' in doc:
                forecastSales = json.loads(doc['forecastSales'])
                filtered_sales = {str(i): forecastSales[str(i)] for i in range(0, (len(forecastSales)-(12-step)))}
                return JSONResponse(content=filtered_sales)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@ForecastRoute.get('/GetForecastProfit')
def get_forecast_profit_route(step:int):
    try:
        docs = collection3.find()
        for doc in docs:
            if 'forecastProfit' in doc:
                forecastProfit = json.loads(doc['forecastProfit'])
                filtered_profit = {str(i): forecastProfit[str(i)] for i in range(0, (len(forecastProfit)-(12-step)))}
                return JSONResponse(content=filtered_profit)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Anomally Definitions
def salesAnomally():
    result = forecastModelSales()
    if 'data' not in result:
        raise Exception("forecastModelSales did not return expected data")
    ad = result['data']
    df = pd.DataFrame(ad, columns=['value'])

    n_estimators = 100  # Number of trees in the forest
    max_samples = 'auto'  # Number of samples to draw to fit each tree
    contamination = 0.15  # Expected proportion of outliers in the data (can be adjusted based on domain knowledge)

    # Initialize Isolation Forest with controllable parameters
    isolation_forest = IsolationForest(n_estimators=n_estimators,
                                    max_samples=max_samples,
                                    contamination=contamination)

    # Fit the model to your data
    isolation_forest.fit(df[['value']])

    # Predict outliers/anomalies
    df['anomaly'] = isolation_forest.predict(df[['value']])

    # Anomalies will be marked as -1, inliers as 1
    anomalies = df[df['anomaly'] == -1]

    # Print or further analyze the anomalies
    return anomalies['value'].to_json()

def profitAnomally():
    result = forecastModelProfit()
    if 'data' not in result:
        raise Exception("forecastModelSales did not return expected data")
    ad = result['data']
    df = pd.DataFrame(ad, columns=['value'])

    n_estimators = 100  # Number of trees in the forest
    max_samples = 'auto'  # Number of samples to draw to fit each tree
    contamination = 0.15  # Expected proportion of outliers in the data (can be adjusted based on domain knowledge)

    # Initialize Isolation Forest with controllable parameters
    isolation_forest = IsolationForest(n_estimators=n_estimators,
                                    max_samples=max_samples,
                                    contamination=contamination)

    # Fit the model to your data
    isolation_forest.fit(df[['value']])

    # Predict outliers/anomalies
    df['anomaly'] = isolation_forest.predict(df[['value']])

    # Anomalies will be marked as -1, inliers as 1
    anomalies = df[df['anomaly'] == -1]

    # Print or further analyze the anomalies
    return anomalies['value'].to_json()


# Anomalies Routes
@ForecastRoute.get('/salesAnomally')
async def salesAnomaly_route():
    return salesAnomally()

@ForecastRoute.get('/profitAnomaly')
async def profitAnomaly_route():
    return profitAnomally()
