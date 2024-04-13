from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from typing import Dict
import json
import pymongo
from functools import lru_cache
from connection import collection4

Top20sRoute = APIRouter()

## What is the best selling product?
@Top20sRoute.get("/product with the most sales")
@lru_cache(maxsize=32)
def get_top20s():
    try:
        docs = collection4.find()
        for doc in docs:
            if 'product_with_the_most_sales' in doc:
                product_with_the_most_sales = json.loads(doc['product_with_the_most_sales'])
                return JSONResponse(content=product_with_the_most_sales)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@Top20sRoute.get("/product with average sales")
@lru_cache(maxsize=32)
def get_top20s():
    try:
        docs = collection4.find()
        for doc in docs:
            if 'product_with_average_sales' in doc:
                product_with_average_sales = json.loads(doc['product_with_average_sales'])
                return JSONResponse(content=product_with_average_sales)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

## Which country has the most sales?
@Top20sRoute.get("/countries with the most sales")
@lru_cache(maxsize=32)
def get_top20s():
    try:
        docs = collection4.find()
        for doc in docs:
            if 'countries_with_the_most_sales' in doc:
                countries_with_the_most_sales = json.loads(doc['countries_with_the_most_sales'])
                return JSONResponse(content=countries_with_the_most_sales)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@Top20sRoute.get("/countries with average sales")
@lru_cache(maxsize=32)
def get_top20s():
    try:
        docs = collection4.find()
        for doc in docs:
            if 'countries_with_average_sales' in doc:
                countries_with_average_sales = json.loads(doc['countries_with_average_sales'])
                return JSONResponse(content=countries_with_average_sales)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
## Which region sold the most?
@Top20sRoute.get("/regions with the most sales")
@lru_cache(maxsize=32)
def get_top20s():
    try:
        docs = collection4.find()
        for doc in docs:
            if 'regions_with_the_most_sales' in doc:
                regions_with_the_most_sales = json.loads(doc['regions_with_the_most_sales'])
                return JSONResponse(content=regions_with_the_most_sales)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@Top20sRoute.get("/regions with average sales")
@lru_cache(maxsize=32)
def get_top20s():
    try:
        docs = collection4.find()
        for doc in docs:
            if 'regions_with_average_sales' in doc:
                regions_with_average_sales = json.loads(doc['regions_with_average_sales'])
                return JSONResponse(content=regions_with_average_sales)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))