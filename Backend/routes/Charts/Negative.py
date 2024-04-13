from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from typing import Dict
import json
import pymongo
from functools import lru_cache
from connection import collection5

NegativeRoute = APIRouter()

@NegativeRoute.get("/best selling products")
@lru_cache(maxsize=32)
def get_negative():
    try:
        docs = collection5.find()
        for doc in docs:
            if 'product_with_the_most_sales' in doc:
                product_with_the_most_sales = json.loads(doc['product_with_the_most_sales'])
                return JSONResponse(content=product_with_the_most_sales)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@NegativeRoute.get("/product_with_average_sales")
@lru_cache(maxsize=32)
def get_negative():
    try:
        docs = collection5.find()
        for doc in docs:
            if 'product_with_average_sales' in doc:
                product_with_average_sales = json.loads(doc['product_with_average_sales'])
                return JSONResponse(content=product_with_average_sales)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@NegativeRoute.get("/Negative order priprity with profit")
@lru_cache(maxsize=32)
def get_negative():
    try:
        docs = collection5.find()
        for doc in docs:
            if 'order_priority_with_profit' in doc:
                order_priority_with_profit = json.loads(doc['order_priority_with_profit'])
                return JSONResponse(content=order_priority_with_profit)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@NegativeRoute.get("/Negative market with profit")
@lru_cache(maxsize=32)
def get_negative():
    try:
        docs = collection5.find()
        for doc in docs:
            if 'market_with_profit' in doc:
                market_with_profit = json.loads(doc['market_with_profit'])
                return JSONResponse(content=market_with_profit)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@NegativeRoute.get("/Negative region with profit")
@lru_cache(maxsize=32)
def get_negative():
    try:
        docs = collection5.find()
        for doc in docs:
            if 'region_with_profit' in doc:
                region_with_profit = json.loads(doc['region_with_profit'])
                return JSONResponse(content=region_with_profit)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@NegativeRoute.get("/Negative category with profit")
@lru_cache(maxsize=32)
def get_negative():
    try:
        docs = collection5.find()
        for doc in docs:
            if 'category_with_profit' in doc:
                category_with_profit = json.loads(doc['category_with_profit'])
                return JSONResponse(content=category_with_profit)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@NegativeRoute.get("/Negative sub_category with profit")
@lru_cache(maxsize=32)
def get_negative():
    try:
        docs = collection5.find()
        for doc in docs:
            if 'sub_category_with_profit' in doc:
                sub_category_with_profit = json.loads(doc['sub_category_with_profit'])
                return JSONResponse(content=sub_category_with_profit)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@NegativeRoute.get("/Negative ship_mode with profit")
@lru_cache(maxsize=32)
def get_negative():
    try:
        docs = collection5.find()
        for doc in docs:
            if 'ship_mode_with_profit' in doc:
                ship_mode_with_profit = json.loads(doc['ship_mode_with_profit'])
                return JSONResponse(content=ship_mode_with_profit)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
