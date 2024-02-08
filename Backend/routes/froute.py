from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from typing import Dict
import json
import pymongo
from functools import lru_cache

froute = APIRouter()

MONGO_URI = "mongodb+srv://shanukafer98:Mongodb123.@cluster0.gtbdj6v.mongodb.net/SSD"
COLLECTION_NAME = "Charts"
client = pymongo.MongoClient(MONGO_URI)
db = client.get_database()
collection = db[COLLECTION_NAME]

@froute.get("/valueCounts_shipMode_Frontend")
@lru_cache(maxsize=32)
def get_shipmode_counts():
    try:
        docs = collection.find()
        for doc in docs:
            if 'ship_mode_counts' in doc:
                ship_mode_counts = json.loads(doc['ship_mode_counts'])
                return JSONResponse(content=ship_mode_counts)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@froute.get("/valueCounts_segment_Frontend")
@lru_cache(maxsize=32)
def get_segment_counts():
    try:
        docs = collection.find()
        for doc in docs:
            if 'segment_counts' in doc:
                segment_counts = json.loads(doc['segment_counts'])
                return JSONResponse(content=segment_counts)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@froute.get("/valueCounts_state_Frontend")
@lru_cache(maxsize=32)
def get_state_counts():
    try:
        docs = collection.find()
        for doc in docs:
            if 'state_counts' in doc:
                state_counts = json.loads(doc['state_counts'])
                return JSONResponse(content=state_counts)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@froute.get("/valueCounts_country_Frontend")
@lru_cache(maxsize=32)
def get_country_counts():
    try:
        docs = collection.find()
        for doc in docs:
            if 'country_counts' in doc:
                country_counts = json.loads(doc['country_counts'])
                return JSONResponse(content=country_counts)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@froute.get("/valueCounts_market_Frontend")
@lru_cache(maxsize=32)
def get_market_counts():
    try:
        docs = collection.find()
        for doc in docs:
            if 'market_counts' in doc:
                market_counts = json.loads(doc['market_counts'])
                return JSONResponse(content=market_counts)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@froute.get("/valueCounts_category_Frontend")
@lru_cache(maxsize=32)
def get_category_counts():
    try:
        docs = collection.find()
        for doc in docs:
            if 'category_counts' in doc:
                category_counts = json.loads(doc['category_counts'])
                return JSONResponse(content=category_counts)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@froute.get("/valueCounts_region_Frontend")
@lru_cache(maxsize=32)
def get_region_counts():
    try:
        docs = collection.find()
        for doc in docs:
            if 'region_counts' in doc:
                region_counts = json.loads(doc['region_counts'])
                return JSONResponse(content=region_counts)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@froute.get("/valueCounts_subCategory_Frontend")
@lru_cache(maxsize=32)
def get_subCategory_counts():
    try:
        docs = collection.find()
        for doc in docs:
            if 'sub_category_counts' in doc:
                sub_category_counts = json.loads(doc['sub_category_counts'])
                return JSONResponse(content=sub_category_counts)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@froute.get("/valueCounts_orderPriority_Frontend")
@lru_cache(maxsize=32)
def get_orderPriority_counts():
    try:
        docs = collection.find()
        for doc in docs:
            if 'order_priority_counts' in doc:
                order_priority_counts = json.loads(doc['order_priority_counts'])
                return JSONResponse(content=order_priority_counts)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))