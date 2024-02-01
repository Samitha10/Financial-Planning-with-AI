from fastapi import FastAPI, APIRouter, HTTPException
import pandas as pd
import pymongo
AutomateRoute = APIRouter()

data= pd.read_csv('fullData.csv')
MONGO_URI = "mongodb+srv://shanukafer98:Mongodb123.@cluster0.gtbdj6v.mongodb.net/SSD"
COLLECTION_NAME = "Charts"
client = pymongo.MongoClient(MONGO_URI)
db = client.get_database()
collection = db[COLLECTION_NAME]

@AutomateRoute.get('/valueCounts_shipMode')
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

@AutomateRoute.get('/valueCounts_segment')
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

@AutomateRoute.get('/valueCounts_state')
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