from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from typing import Dict
import json
import pymongo
from functools import lru_cache

valueCountsRoute = APIRouter()

from connection import collection

# Now you have the minimum and maximum year and month values
# Use these values to define the range
@valueCountsRoute.get("/FullTimePeriod_Frontend")
@lru_cache(maxsize=32)
def full_timeperiod():
    try:
        # Initialize min_year, min_month, max_year, max_month with extreme values
        min_year = float('inf')
        min_month = float('inf')
        max_year = float('-inf')
        max_month = float('-inf')

        # Find the minimum and maximum year and month in the dataset
        docs = collection.find()
        for doc in docs:
            if 'ship_mode_counts' in doc:
                counts = json.loads(doc['ship_mode_counts'])
                for key in counts.keys():
                    year, month, _ = key.strip("()").split(", ")
                    year = int(year)
                    month = int(month)
                    min_year = min(min_year, year)
                    min_month = min(min_month, month)
                    max_year = max(max_year, year)
                    max_month = max(max_month, month)

        return min_year, min_month, max_year, max_month

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@valueCountsRoute.get("/valueCounts_shipMode_Frontend")
@lru_cache(maxsize=32)
def get_shipmode_counts_within_range(start_year: int, start_month: int, end_year: int, end_month: int):
    try:
        # Filter documents based on the year and month range
        docs = collection.find()

        # Initialize ship_mode_counts dictionary
        ship_mode_counts = {}

        # Extract ship mode counts from filtered documents
        for doc in docs:
            if 'ship_mode_counts' in doc:
                counts = json.loads(doc['ship_mode_counts'])
                for key, value in counts.items():
                    # Parse year, month, and ship mode from the key
                    key = key.strip("()").replace("'", "").split(", ")
                    year = int(key[0])
                    month = int(key[1])
                    ship_mode = key[2]

                    # Check if the year and month are within the specified range
                    if (start_year <= year <= end_year) or \
                        (start_year == year and start_month <= month) or \
                        (end_year == year and month <= end_month) or \
                        (start_year == year == end_year and start_month <= month <= end_month):
                        # Create a new key with the ship mode as a string
                        new_key = f"({year}, {month}, '{ship_mode}')"
                        ship_mode_counts[new_key] = value



        if ship_mode_counts:
            return JSONResponse(content=ship_mode_counts)
        else:
            return {"message": "No data found for the specified time period"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@valueCountsRoute.get("/valueCounts_segment_Frontend")
@lru_cache(maxsize=32)
def get_segment_counts_within_range(start_year: int, start_month: int, end_year: int, end_month: int):
    try:
        # Filter documents based on the year and month range
        docs = collection.find()

        # Initialize segment_counts dictionary
        segment_counts = {}

        # Extract segment counts from filtered documents
        for doc in docs:
            if 'segment_counts' in doc:
                counts = json.loads(doc['segment_counts'])
                for key, value in counts.items():
                    # Parse year and month from the key
                    year, month, _ = key.strip("()").split(", ")
                    year = int(year)
                    month = int(month)

                    # Check if the year and month are within the specified range
                    if (start_year < year < end_year) or \
                            (start_year == year and start_month <= month) or \
                            (end_year == year and month <= end_month):
                        segment_counts[key] = value

        if segment_counts:
            return JSONResponse(content=segment_counts)
        else:
            return {"message": "No data found for the specified time period"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@valueCountsRoute.get("/valueCounts_state_Frontend")
@lru_cache(maxsize=32)
def get_state_counts_within_range(start_year: int, start_month: int, end_year: int, end_month: int):
    try:
        # Filter documents based on the year and month range
        docs = collection.find()

        # Initialize state_counts dictionary
        state_counts = {}

        # Extract state counts from filtered documents
        for doc in docs:
            if 'state_counts' in doc:
                counts = json.loads(doc['state_counts'])
                for key, value in counts.items():
                    # Parse year and month from the key
                    year, month, _ = key.strip("()").split(", ")
                    year = int(year)
                    month = int(month)

                    # Check if the year and month are within the specified range
                    if (start_year < year < end_year) or \
                            (start_year == year and start_month <= month) or \
                            (end_year == year and month <= end_month):
                        state_counts[key] = value

        if state_counts:
            return JSONResponse(content=state_counts)
        else:
            return {"message": "No data found for the specified time period"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@valueCountsRoute.get("/valueCounts_country_Frontend")
@lru_cache(maxsize=32)
def get_country_counts_within_range(start_year: int, start_month: int, end_year: int, end_month: int):
    try:
        # Filter documents based on the year and month range
        docs = collection.find()

        # Initialize country_counts dictionary
        country_counts = {}

        # Extract country counts from filtered documents
        for doc in docs:
            if 'country_counts' in doc:
                counts = json.loads(doc['country_counts'])
                for key, value in counts.items():
                    # Parse year and month from the key
                    year, month, _ = key.strip("()").split(", ")
                    year = int(year)
                    month = int(month)

                    # Check if the year and month are within the specified range
                    if (start_year < year < end_year) or \
                            (start_year == year and start_month <= month) or \
                            (end_year == year and month <= end_month):
                        country_counts[key] = value

        if country_counts:
            return JSONResponse(content=country_counts)
        else:
            return {"message": "No data found for the specified time period"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@valueCountsRoute.get("/valueCounts_market_Frontend")
@lru_cache(maxsize=32)
def get_market_counts_within_range(start_year: int, start_month: int, end_year: int, end_month: int):
    try:
        # Filter documents based on the year and month range
        docs = collection.find()

        # Initialize market_counts dictionary
        market_counts = {}

        # Extract market counts from filtered documents
        for doc in docs:
            if 'market_counts' in doc:
                counts = json.loads(doc['market_counts'])
                for key, value in counts.items():
                    # Parse year and month from the key
                    year, month, _ = key.strip("()").split(", ")
                    year = int(year)
                    month = int(month)

                    # Check if the year and month are within the specified range
                    if (start_year < year < end_year) or \
                            (start_year == year and start_month <= month) or \
                            (end_year == year and month <= end_month):
                        market_counts[key] = value

        if market_counts:
            return JSONResponse(content=market_counts)
        else:
            return {"message": "No data found for the specified time period"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@valueCountsRoute.get("/valueCounts_category_Frontend")
@lru_cache(maxsize=32)
def get_category_counts_within_range(start_year: int, start_month: int, end_year: int, end_month: int):
    try:
        # Filter documents based on the year and month range
        docs = collection.find()

        # Initialize category_counts dictionary
        category_counts = {}

        # Extract category counts from filtered documents
        for doc in docs:
            if 'category_counts' in doc:
                counts = json.loads(doc['category_counts'])
                for key, value in counts.items():
                    # Parse year and month from the key
                    year, month, _ = key.strip("()").split(", ")
                    year = int(year)
                    month = int(month)

                    # Check if the year and month are within the specified range
                    if (start_year < year < end_year) or \
                            (start_year == year and start_month <= month) or \
                            (end_year == year and month <= end_month):
                        category_counts[key] = value

        if category_counts:
            return JSONResponse(content=category_counts)
        else:
            return {"message": "No data found for the specified time period"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@valueCountsRoute.get("/valueCounts_region_Frontend")
@lru_cache(maxsize=32)
def get_region_counts_within_range(start_year: int, start_month: int, end_year: int, end_month: int):
    try:
        # Filter documents based on the year and month range
        docs = collection.find()

        # Initialize region_counts dictionary
        region_counts = {}

        # Extract region counts from filtered documents
        for doc in docs:
            if 'region_counts' in doc:
                counts = json.loads(doc['region_counts'])
                for key, value in counts.items():
                    year, month, _ = key.strip("()").split(", ")
                    year = int(year)
                    month = int(month)

                    # Check if the year and month are within the specified range
                    if (start_year < year < end_year) or \
                            (start_year == year and start_month <= month) or \
                            (end_year == year and month <= end_month):
                        region_counts[key] = value

        if region_counts:
            return JSONResponse(content=region_counts)
        else:
            return {"message": "No data found for the specified time period"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@valueCountsRoute.get("/valueCounts_subCategory_Frontend")
@lru_cache(maxsize=32)
def get_subCategory_counts_within_range(start_year: int, start_month: int, end_year: int, end_month: int):
    try:
        # Filter documents based on the year and month range
        docs = collection.find()

        # Initialize sub_category_counts dictionary
        sub_category_counts = {}

        # Extract subCategory counts from filtered documents
        for doc in docs:
            if 'sub_category_counts' in doc:
                counts = json.loads(doc['sub_category_counts'])
                for key, value in counts.items():
                    year, month, _ = key.strip("()").split(", ")
                    year = int(year)
                    month = int(month)

                    # Check if the year and month are within the specified range
                    if (start_year < year < end_year) or \
                            (start_year == year and start_month <= month) or \
                            (end_year == year and month <= end_month):
                        sub_category_counts[key] = value

        if sub_category_counts:
            return JSONResponse(content=sub_category_counts)
        else:
            return {"message": "No data found for the specified time period"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@valueCountsRoute.get("/valueCounts_orderPriority_Frontend")
@lru_cache(maxsize=32)
def get_orderPriority_counts_within_range(start_year: int, start_month: int, end_year: int, end_month: int):
    try:
        # Filter documents based on the year and month range
        docs = collection.find()

        # Initialize order_priority_counts dictionary
        order_priority_counts = {}

        # Extract orderPriority counts from filtered documents
        for doc in docs:
            if 'order_priority_counts' in doc:
                counts = json.loads(doc['order_priority_counts'])
                for key, value in counts.items():
                    year, month, _ = key.strip("()").split(", ")
                    year = int(year)
                    month = int(month)

                    # Check if the year and month are within the specified range
                    if (start_year < year < end_year) or \
                            (start_year == year and start_month <= month) or \
                            (end_year == year and month <= end_month):
                        order_priority_counts[key] = value

        if order_priority_counts:
            return JSONResponse(content=order_priority_counts)
        else:
            return {"message": "No data found for the specified time period"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    
# Customer and Product_id Counts
@valueCountsRoute.get("/Unique_customer_id_Frontend")
@lru_cache(maxsize=32)
def get_customer_id_counts():
    try:
        docs = collection.find()
        for doc in docs:
            if 'Customer_id_counts' in doc:
                Customer_id_counts = json.loads(doc['Customer_id_counts'])
                return JSONResponse(content=Customer_id_counts)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@valueCountsRoute.get("/valueCounts_product_id_Frontend")
@lru_cache(maxsize=32)
def get_product_id_counts():
    try:
        docs = collection.find()
        for doc in docs:
            if 'Product_id_counts' in doc:
                Product_id_counts = json.loads(doc['Product_id_counts'])
                return JSONResponse(content=Product_id_counts)
        return {"message": "No data found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))