from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import Dict
import json,pymongo
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
    # Assuming 'ship_mode' is the name of your collection
    doc =collection.find_one()
    if doc is not None:
        ship_mode_counts = json.loads(doc['ship_mode_counts'])
        return JSONResponse(content=ship_mode_counts)
    else:
        return {"message": "No data found"}