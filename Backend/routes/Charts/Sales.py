from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from typing import Dict
import json
import pymongo
from functools import lru_cache

SalesRoute = APIRouter()

MONGO_URI = "mongodb+srv://shanukafer98:Mongodb123.@cluster0.gtbdj6v.mongodb.net/SSD"
COLLECTION_NAME = "Charts"
client = pymongo.MongoClient(MONGO_URI)
db = client.get_database()
collection = db[COLLECTION_NAME]

@SalesRoute.get("/Sales_Frontend")
@lru_cache(maxsize=32)
def get_sales():
    try:
        docs = collection.find()
        for doc in docs:
            if 'YMsales' in doc:
                YMsales = json.loads(doc['YMsales'])
                return JSONResponse(content=YMsales)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))