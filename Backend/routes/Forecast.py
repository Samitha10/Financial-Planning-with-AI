import pickle, json
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from connection import collection3, data
import numpy as np
import pandas as pd

ForecastRoute = APIRouter()

with open('models/Sales.pkl','rb') as file:
  model1 = pickle.load(file)
with open('models/Profit.pkl','rb') as file:
  model2 = pickle.load(file)

# Sales Forecast and Send to MongoDB
@ForecastRoute.post('/forecastSales')
async def forecast_route():
    # Use the forecasting function to generate predictions
    forecast_steps = 36
    forecast = model1.get_forecast(steps=forecast_steps)
    predictions = forecast.predicted_mean
    pastData = data.groupby(['year', 'month']).agg({'sales': 'sum'}).reset_index()
    fullPredictions = pd.concat([pastData['sales'], predictions], axis=0)
    # Send the predictions to MongoDB
    try:
        collection3.delete_many({"forecastSales": {"$exists": True}})
        collection3.insert_one({"forecastSales": fullPredictions.to_json()})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}
        
# Profit Forecast and Send to MongoDB    
@ForecastRoute.post('/forecastProfit')
async def forecast_profit_route():
    # Use the forecasting function to generate predictions
    forecast_steps = 36
    forecast = model2.get_forecast(steps=forecast_steps)
    predictions = forecast.predicted_mean
    pastData = data.groupby(['year', 'month']).agg({'profit': 'sum'}).reset_index()
    fullPredictions = pd.concat([pastData['profit'], predictions], axis=0)
    # Send the predictions to MongoDB
    try:
        collection3.delete_many({"forecastProfit": {"$exists": True}})
        collection3.insert_one({"forecastProfit": fullPredictions.to_json()})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}


@ForecastRoute.get('/GetForecastSales')
def get_forecast_route():
    try:
        docs = collection3.find()
        for doc in docs:
            if 'forecastSales' in doc:
                forecastSales = json.loads(doc['forecastSales'])
                return JSONResponse(content=forecastSales)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@ForecastRoute.get('/GetForecastProfit')
def get_forecast_profit_route():
    try:
        docs = collection3.find()
        for doc in docs:
            if 'forecastProfit' in doc:
                forecastProfit = json.loads(doc['forecastProfit'])
                return JSONResponse(content=forecastProfit)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))