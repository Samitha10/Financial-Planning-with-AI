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


    try:
        docs = collection.find()
        for doc in docs:
            if 'order_priority_counts' in doc:
                order_priority_counts = json.loads(doc['order_priority_counts'])
                return JSONResponse(content=order_priority_counts)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))