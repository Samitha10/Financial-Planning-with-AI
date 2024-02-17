from fastapi import FastAPI, APIRouter, HTTPException
import pandas as pd
import pymongo
AutomateRoute = APIRouter()

from connection import data, MONGO_URI, COLLECTION_NAME, client, db, collection

@AutomateRoute.post('/valueCounts_shipMode')
def valueCounts_shipMode():
    try:
        data1 = data['ship_mode'].value_counts().to_json()
        # Delete all documents that have the key "ship_mode_counts"
        collection.delete_many({"ship_mode_counts": {"$exists": True}})
        # Insert the new document
        collection.insert_one({"ship_mode_counts": data1})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/valueCounts_segment')
def valueCounts_segment():
    try:
        data2 = data['segment'].value_counts().to_json()
        # Delete all documents that have the key "segment_counts"
        collection.delete_many({"segment_counts": {"$exists": True}})
        # Insert the new document
        collection.insert_one({"segment_counts": data2})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/valueCounts_state')
def valueCounts_state():
    try:
        data3 = data['state'].value_counts().to_json()
        # Delete all documents that have the key "state_counts"
        collection.delete_many({"state_counts": {"$exists": True}})
        # Insert the new document
        collection.insert_one({"state_counts": data3})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/valueCounts_country')
def valueCounts_country():
    try:
        data4 = data['country'].value_counts().to_json()
        # Delete all documents that have the key "country_counts"
        collection.delete_many({"country_counts": {"$exists": True}})
        # Insert the new document
        collection.insert_one({"country_counts": data4})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/valueCounts_market')
def valueCounts_market():
    try:
        data5 = data['market'].value_counts().to_json()
        # Delete all documents that have the key "market_counts"
        collection.delete_many({"market_counts": {"$exists": True}})
        # Insert the new document
        collection.insert_one({"market_counts": data5})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/valueCounts_region')
def valueCounts_region():
    try:
        data6 = data['region'].value_counts().to_json()
        # Delete all documents that have the key "region_counts"
        collection.delete_many({"region_counts": {"$exists": True}})
        # Insert the new document
        collection.insert_one({"region_counts": data6})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/valueCounts_category')
def valueCounts_category():
    try:
        data7 = data['category'].value_counts().to_json()
        # Delete all documents that have the key "category_counts"
        collection.delete_many({"category_counts": {"$exists": True}})
        # Insert the new document
        collection.insert_one({"category_counts": data7})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/valueCounts_subCategory')
def valueCounts_subCategory():
    try:
        data8 = data['sub_category'].value_counts().to_json()
        # Delete all documents that have the key "sub_category_counts"
        collection.delete_many({"sub_category_counts": {"$exists": True}})
        # Insert the new document
        collection.insert_one({"sub_category_counts": data8})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/valueCounts_orderPriority')
def valueCounts_orderPriority():
    try:
        data9 = data['order_priority'].value_counts().to_json()
        # Delete all documents that have the key "order_priority_counts"
        collection.delete_many({"order_priority_counts": {"$exists": True}})
        # Insert the new document
        collection.insert_one({"order_priority_counts": data9})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/YMSales')
def Sales():
    try:
        
        data10 = data.groupby(['year', 'month']).agg({'fsales': 'sum'}).reset_index().to_json()
        # Delete all documents that have the key "sales"
        collection.delete_many({"YMsales": {"$exists": True}})
        # Insert the new document
        collection.insert_one({"YMsales": data10})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/YMProfit')
def Profit():
    try:
        data11 = data.groupby(['year', 'month']).agg({'profit': 'sum'}).reset_index().to_json()
        # Delete all documents that have the key "profit"
        collection.delete_many({"YMprofit": {"$exists": True}})
        # Insert the new document
        collection.insert_one({"YMprofit": data11})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}