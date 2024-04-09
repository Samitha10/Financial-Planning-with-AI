import pickle, json
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from connection import collection3

ForecastRoute = APIRouter()

with open('models/Sales.pkl','rb') as file:
  model1 = pickle.load(file)
with open('models/Profit.pkl','rb') as file:
  model2 = pickle.load(file)

@ForecastRoute.post('/forecastSales')
async def forecast_route(periods: int):
    # Use the forecasting function to generate predictions
    forecast_steps = periods
    forecast = model1.get_forecast(steps=forecast_steps)
    predictions = forecast.predicted_mean
    # Send the predictions to MongoDB
    try:
        collection3.delete_many({"forecastSales": {"$exists": True}})
        collection3.insert_one({"forecastSales": predictions.to_json()})
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
    
@ForecastRoute.post('/forecastProfit')
async def forecast_profit_route(periods: int):
    # Use the forecasting function to generate predictions
    forecast_steps = periods
    forecast = model2.get_forecast(steps=forecast_steps)
    predictions = forecast.predicted_mean
    # Send the predictions to MongoDB
    try:
        collection3.delete_many({"forecastProfit": {"$exists": True}})
        collection3.insert_one({"forecastProfit": predictions.to_json()})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

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