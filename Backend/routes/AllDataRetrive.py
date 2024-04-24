from fastapi import APIRouter, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
import asyncio
import pymongo
from pymongo.server_api import ServerApi
from bson import ObjectId

from connection import MONGO_URI2, MONGO_URI
AllDataRetriveRoute = APIRouter()

class Item(BaseModel):
    order_id: str
    product_id: str

import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

@AllDataRetriveRoute.get("/search")
async def search_data(order_id: str, product_id: str):
    # Replace the placeholder with your Atlas connection string
    uri = MONGO_URI2
    # Set the Stable API version when creating a new client
    client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
    db = client['SSD']
    collection = db['Super_Store_Data']  # Replace 'your_collection_name' with your actual collection name
    try:
        # Search for documents matching the product_id and order_id
        cursor = collection.find({ "order_id": order_id, "product_id": product_id })
        results = await cursor.to_list(length=100)

        # Convert ObjectId to string
        for document in results:
            document['_id'] = str(document['_id'])

        return results

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


from bson import json_util
import json

@AllDataRetriveRoute.get("/Pymongo")
def retrieve_first_10_rows():
    # Connect to the MongoDB server
    client = pymongo.MongoClient(MONGO_URI)
    db = client.get_database()

    COLLECTION_NAME1 = "Super_Store_Data"
    collection = db[COLLECTION_NAME1]

    # Retrieve the first 10 rows
    rows = list(collection.find().limit(10))

    # Convert ObjectId to string
    rows = json.loads(json_util.dumps(rows))

    return rows


from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

class DataRetriever:
    call_count = 0  # Initialize a class variable to keep track of the number of calls
    step = 2  # Define the step size

    @AllDataRetriveRoute.get("/DataRetrive")
    async def retrieve_rows_in_range():
        DataRetriever.call_count += 1  # Increment the call count
        client = AsyncIOMotorClient(MONGO_URI)
        db = client.get_database()

        COLLECTION_NAME1 = "Super_Store_Data"
        collection = db[COLLECTION_NAME1]

        # Calculate the starting and ending indices of the range
        start_index = (DataRetriever.call_count - 1) * DataRetriever.step

        # Retrieve data within the specified range
        rows = await collection.find().skip(start_index).limit(DataRetriever.step).to_list(None)

        # Convert ObjectId to string
        for row in rows:
            row['_id'] = str(row['_id'])

        return rows

@AllDataRetriveRoute.delete("/delete/{row_id}")
async def delete_row(row_id: str):
    # Replace the placeholder with your Atlas connection string
    uri = MONGO_URI2
    # Set the Stable API version when creating a new client
    client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
    db = client['SSD']
    collection = db['Super_Store_Data']  # Replace 'your_collection_name' with your actual collection name
    try:
        # Delete the document with the specified row_id
        result = await collection.delete_one({ "_id": ObjectId(row_id) })

        if result.deleted_count == 1:
            return {"message": "Row deleted successfully"}
        else:
            return {"message": "Row not found"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
from bson.objectid import ObjectId

@AllDataRetriveRoute.put("/update/{row_id}")
async def update_row(row_id: str, data: dict):
    # Replace the placeholder with your Atlas connection string
    uri = MONGO_URI2
    # Set the Stable API version when creating a new client
    client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
    db = client['SSD']
    collection = db['Super_Store_Data']

    # Convert row_id to ObjectId
    row_id_obj = ObjectId(row_id)

    # Update the document with the specified _id
    result = await collection.update_one({'_id': row_id_obj}, {'$set': data})

    if result.modified_count == 1:
        return {"message": "Document updated successfully"}
    else:
        return {"message": "No document found or document not updated"}
