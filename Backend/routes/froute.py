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
def get_ship_mode_counts():
    try:
        docs = collection.find()
        for doc in docs:
            if 'ship_mode_counts' in doc:
                ship_mode_counts = json.loads(doc['ship_mode_counts'])
                return JSONResponse(content=ship_mode_counts)
            return {"message": "No data found"}
    except Exception as e:
        return {"message": str(e)}


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