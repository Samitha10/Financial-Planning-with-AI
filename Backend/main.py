import traceback
from fastapi import FastAPI, HTTPException,APIRouter
import pymongo
from pymongo.mongo_client import MongoClient
import pandas as pd
import traceback
from fastapi.middleware.cors import CORSMiddleware

from AllCharts.Charts import router1
from AllCharts.bar import router2
from AllCharts.froute import router3

app = FastAPI()
app.include_router(router1)
app.include_router(router2)
app.include_router(router3)


origins = [
    "http://localhost:3000",  # React app address
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def one():
    return {'one one bbbbbbbbbbbbbbbbb'}

{# url = "mongodb+srv://shanukafer98:Mongodb123.@cluster0.gtbdj6v.mongodb.net/?retryWrites=true&w=majority"  
# client = MongoClient(url)
# db = client.SSD
# collection = db.Super_Store_Data

# @app.get('/getdata')
# def getdata():
#     try:
#         result = list(collection.find())
#         # Convert ObjectId to str for serialization
#         for doc in result:
#             if "_id" in doc:
#                 doc["_id"] = str(doc["_id"])
#         df = pd.DataFrame(result)
#         # Drop the '_id' column from the DataFrame
#         df = df.drop("_id", axis=1)

#     except Exception as e:
#         print(f"Exception: {str(e)}")
#         traceback.print_exc()
#         raise HTTPException(status_code=500, detail="Internal Server Error")
    
#     df.to_csv('fullData.csv',index=True)

#     # Convert the modified DataFrame to a dictionary
#     result1 = df.to_dict(orient='records')

#     return {"data": result1}
}

@app.get('/data')
def chart1():
    try:
        df1 = pd.read_csv('fullData.csv')
        data1 = df1['ship_mode'].value_counts().to_json()

        MONGO_URI = "mongodb+srv://shanukafer98:Mongodb123.@cluster0.gtbdj6v.mongodb.net/SSD"
        COLLECTION_NAME = "ship_mode"
        client = pymongo.MongoClient(MONGO_URI)
        db = client.get_database()
        collection = db[COLLECTION_NAME]
        # Delete all documents that have the key "ship_mode_counts"
        collection.delete_many({"ship_mode_counts": {"$exists": True}})
        # Insert the new document
        collection.insert_one({"ship_mode_counts": data1})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}
