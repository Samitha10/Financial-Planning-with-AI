from fastapi import FastAPI, HTTPException,APIRouter
import pymongo, traceback
from pymongo.mongo_client import MongoClient
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

from routes.Automate import AutomateRoute
from routes.froute import froute

app = FastAPI()
app.include_router(froute, prefix="/froute", tags=["froute"])
app.include_router(AutomateRoute, prefix="/automate", tags=["automate"])


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
    return {'This is first api':'Hello World'}

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

