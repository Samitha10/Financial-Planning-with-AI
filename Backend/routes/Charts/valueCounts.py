from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from typing import Dict
import json
import pymongo
from functools import lru_cache

valueCountsRoute = APIRouter()

from connection import collection

# Now you have the minimum and maximum year and month values
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

# Use these values to define the range
@valueCountsRoute.get("/FullTimePeriod_Frontend")
@lru_cache(maxsize=32)
def get_full_timeperiod():
    return full_timeperiod()
    

from datetime import datetime
@valueCountsRoute.get("/valueCounts_shipMode_Frontend")
@lru_cache(maxsize=32)
def get_shipmode_counts_within_range(start_year: int, start_month: int, end_year: int, end_month: int):
    try: 
        # Convert start and end dates to comparable format
        min_year, min_month, max_year, max_month = full_timeperiod()
        start_date = datetime(min_year, min_month, 1)
        end_date = datetime(max_year, max_month, 1)

        # Check if the start and end dates are within the range
        current_date1 = datetime(start_year, start_month, 1)
        current_date2 = datetime(end_year, end_month, 1)

        if start_date<=current_date1 and current_date2<=end_date:
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
                        # Check if the year and month are within the range
                        if current_date1 <= datetime(year, month, 1) <= current_date2:
                            # Add the count to the corresponding ship mode
                            if ship_mode in ship_mode_counts:
                                ship_mode_counts[ship_mode] += value
                            else:
                                ship_mode_counts[ship_mode] = value
                    return JSONResponse(content=ship_mode_counts)
        else:
            return {"message": "No data found for the specified time period"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@valueCountsRoute.get("/valueCounts_segment_Frontend")
@lru_cache(maxsize=32)
def get_segment_counts_within_range(start_year: int, start_month: int, end_year: int, end_month: int):
    try:
        # Convert start and end dates to comparable format
        min_year, min_month, max_year, max_month = full_timeperiod()
        start_date = datetime(min_year, min_month, 1)
        end_date = datetime(max_year, max_month, 1)

        # Check if the start and end dates are within the range
        current_date1 = datetime(start_year, start_month, 1)
        current_date2 = datetime(end_year, end_month, 1)

        if start_date<=current_date1 and current_date2<=end_date:
            # Filter documents based on the year and month range
            docs = collection.find()

            # Initialize segment_counts dictionary
            segment_counts = {}

            # Extract segment counts from filtered documents
            for doc in docs:
                if 'segment_counts' in doc:
                    counts = json.loads(doc['segment_counts'])
                    for key, value in counts.items():
                        # Parse year, month, and segment from the key
                        key = key.strip("()").replace("'", "").split(", ")
                        year = int(key[0])
                        month = int(key[1])
                        segment = key[2]
                        # Check if the year and month are within the range
                        if current_date1 <= datetime(year, month, 1) <= current_date2:
                            # Add the count to the corresponding segment
                            if segment in segment_counts:
                                segment_counts[segment] += value
                            else:
                                segment_counts[segment] = value
                    return JSONResponse(content=segment_counts)
        else:
            return {"message": "No data found for the specified time period"}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@valueCountsRoute.get("/valueCounts_state_Frontend")
@lru_cache(maxsize=32)
def get_state_counts_within_range(start_year: int, start_month: int, end_year: int, end_month: int):
    try:
        # Convert start and end dates to comparable format
        min_year, min_month, max_year, max_month = full_timeperiod()
        start_date = datetime(min_year, min_month, 1)
        end_date = datetime(max_year, max_month, 1)

        # Check if the start and end dates are within the range
        current_date1 = datetime(start_year, start_month, 1)
        current_date2 = datetime(end_year, end_month, 1)

        if start_date<=current_date1 and current_date2<=end_date:
            # Filter documents based on the year and month range
            docs = collection.find()

            # Initialize state_counts dictionary
            state_counts = {}

            # Extract state counts from filtered documents
            for doc in docs:
                if 'state_counts' in doc:
                    counts = json.loads(doc['state_counts'])
                    for key, value in counts.items():
                        # Parse year, month, and state from the key
                        key = key.strip("()").replace("'", "").split(", ")
                        year = int(key[0])
                        month = int(key[1])
                        state = key[2]
                        # Check if the year and month are within the range
                        if current_date1 <= datetime(year, month, 1) <= current_date2:
                            # Add the count to the corresponding state
                            if state in state_counts:
                                state_counts[state] += value
                            else:
                                state_counts[state] = value
                    return JSONResponse(content=state_counts)
        else:
            return {"message": "No data found for the specified time period"}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@valueCountsRoute.get("/valueCounts_country_Frontend")
@lru_cache(maxsize=32)
def get_country_counts_within_range(start_year: int, start_month: int, end_year: int, end_month: int):
    try:
        # Convert start and end dates to comparable format
        min_year, min_month, max_year, max_month = full_timeperiod()
        start_date = datetime(min_year, min_month, 1)
        end_date = datetime(max_year, max_month, 1)

        # Check if the start and end dates are within the range
        current_date1 = datetime(start_year, start_month, 1)
        current_date2 = datetime(end_year, end_month, 1)

        if start_date<=current_date1 and current_date2<=end_date:
            # Filter documents based on the year and month range
            docs = collection.find()

            # Initialize country_counts dictionary
            country_counts = {}

            # Extract country counts from filtered documents
            for doc in docs:
                if 'country_counts' in doc:
                    counts = json.loads(doc['country_counts'])
                    for key, value in counts.items():
                        # Parse year, month, and country from the key
                        key = key.strip("()").replace("'", "").split(", ")
                        year = int(key[0])
                        month = int(key[1])
                        country = key[2]
                        # Check if the year and month are within the range
                        if current_date1 <= datetime(year, month, 1) <= current_date2:
                            # Add the count to the corresponding country
                            if country in country_counts:
                                country_counts[country] += value
                            else:
                                country_counts[country] = value
                    return JSONResponse(content=country_counts)
        else:
            return {"message": "No data found for the specified time period"}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@valueCountsRoute.get("/valueCounts_market_Frontend")
@lru_cache(maxsize=32)
def get_market_counts_within_range(start_year: int, start_month: int, end_year: int, end_month: int):
    try:
        # Convert start and end dates to comparable format
        min_year, min_month, max_year, max_month = full_timeperiod()
        start_date = datetime(min_year, min_month, 1)
        end_date = datetime(max_year, max_month, 1)

        # Check if the start and end dates are within the range
        current_date1 = datetime(start_year, start_month, 1)
        current_date2 = datetime(end_year, end_month, 1)

        if start_date<=current_date1 and current_date2<=end_date:
            # Filter documents based on the year and month range
            docs = collection.find()

            # Initialize market_counts dictionary
            market_counts = {}

            # Extract market counts from filtered documents
            for doc in docs:
                if 'market_counts' in doc:
                    counts = json.loads(doc['market_counts'])
                    for key, value in counts.items():
                        # Parse year, month, and market from the key
                        key = key.strip("()").replace("'", "").split(", ")
                        year = int(key[0])
                        month = int(key[1])
                        market = key[2]
                        # Check if the year and month are within the range
                        if current_date1 <= datetime(year, month, 1) <= current_date2:
                            # Add the count to the corresponding market
                            if market in market_counts:
                                market_counts[market] += value
                            else:
                                market_counts[market] = value
                    return JSONResponse(content=market_counts)
        else:
            return {"message": "No data found for the specified time period"}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@valueCountsRoute.get("/valueCounts_category_Frontend")
@lru_cache(maxsize=32)
def get_category_counts_within_range(start_year: int, start_month: int, end_year: int, end_month: int):
    try:
        # Convert start and end dates to comparable format
        min_year, min_month, max_year, max_month = full_timeperiod()
        start_date = datetime(min_year, min_month, 1)
        end_date = datetime(max_year, max_month, 1)

        # Check if the start and end dates are within the range
        current_date1 = datetime(start_year, start_month, 1)
        current_date2 = datetime(end_year, end_month, 1)

        if start_date<=current_date1 and current_date2<=end_date:
            # Filter documents based on the year and month range
            docs = collection.find()

            # Initialize category_counts dictionary
            category_counts = {}

            # Extract category counts from filtered documents
            for doc in docs:
                if 'category_counts' in doc:
                    counts = json.loads(doc['category_counts'])
                    for key, value in counts.items():
                        # Parse year, month, and category from the key
                        key = key.strip("()").replace("'", "").split(", ")
                        year = int(key[0])
                        month = int(key[1])
                        category = key[2]
                        # Check if the year and month are within the range
                        if current_date1 <= datetime(year, month, 1) <= current_date2:
                            # Add the count to the corresponding category
                            if category in category_counts:
                                category_counts[category] += value
                            else:
                                category_counts[category] = value
                    return JSONResponse(content=category_counts)
        else:
            return {"message": "No data found for the specified time period"}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@valueCountsRoute.get("/valueCounts_region_Frontend")
@lru_cache(maxsize=32)
def get_region_counts_within_range(start_year: int, start_month: int, end_year: int, end_month: int):
    try:
        # Convert start and end dates to comparable format
        min_year, min_month, max_year, max_month = full_timeperiod()
        start_date = datetime(min_year, min_month, 1)
        end_date = datetime(max_year, max_month, 1)

        # Check if the start and end dates are within the range
        current_date1 = datetime(start_year, start_month, 1)
        current_date2 = datetime(end_year, end_month, 1)

        if start_date<=current_date1 and current_date2<=end_date:
            # Filter documents based on the year and month range
            docs = collection.find()

            # Initialize region_counts dictionary
            region_counts = {}

            # Extract region counts from filtered documents
            for doc in docs:
                if 'region_counts' in doc:
                    counts = json.loads(doc['region_counts'])
                    for key, value in counts.items():
                        # Parse year, month, and region from the key
                        key = key.strip("()").replace("'", "").split(", ")
                        year = int(key[0])
                        month = int(key[1])
                        region = key[2]
                        # Check if the year and month are within the range
                        if current_date1 <= datetime(year, month, 1) <= current_date2:
                            # Add the count to the corresponding region
                            if region in region_counts:
                                region_counts[region] += value
                            else:
                                region_counts[region] = value
                    return JSONResponse(content=region_counts)
        else:
            return {"message": "No data found for the specified time period"}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@valueCountsRoute.get("/valueCounts_subCategory_Frontend")
@lru_cache(maxsize=32)
def get_sub_category_counts_within_range(start_year: int, start_month: int, end_year: int, end_month: int):
    try:
        # Convert start and end dates to comparable format
        min_year, min_month, max_year, max_month = full_timeperiod()
        start_date = datetime(min_year, min_month, 1)
        end_date = datetime(max_year, max_month, 1)

        # Check if the start and end dates are within the range
        current_date1 = datetime(start_year, start_month, 1)
        current_date2 = datetime(end_year, end_month, 1)

        if start_date<=current_date1 and current_date2<=end_date:
            # Filter documents based on the year and month range
            docs = collection.find()

            # Initialize sub_category_counts dictionary
            sub_category_counts = {}

            # Extract subCategory counts from filtered documents
            for doc in docs:
                if 'sub_category_counts' in doc:
                    counts = json.loads(doc['sub_category_counts'])
                    for key, value in counts.items():
                        # Parse year, month, and subCategory from the key
                        key = key.strip("()").replace("'", "").split(", ")
                        year = int(key[0])
                        month = int(key[1])
                        subCategory = key[2]
                        # Check if the year and month are within the range
                        if current_date1 <= datetime(year, month, 1) <= current_date2:
                            # Add the count to the corresponding subCategory
                            if subCategory in sub_category_counts:
                                sub_category_counts[subCategory] += value
                            else:
                                sub_category_counts[subCategory] = value
                    return JSONResponse(content=sub_category_counts)
        else:
            return {"message": "No data found for the specified time period"}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@valueCountsRoute.get("/valueCounts_orderPriority_Frontend")
@lru_cache(maxsize=32)
def get_order_priority_counts_within_range(start_year: int, start_month: int, end_year: int, end_month: int):
    try:
        # Convert start and end dates to comparable format
        min_year, min_month, max_year, max_month = full_timeperiod()
        start_date = datetime(min_year, min_month, 1)
        end_date = datetime(max_year, max_month, 1)

        # Check if the start and end dates are within the range
        current_date1 = datetime(start_year, start_month, 1)
        current_date2 = datetime(end_year, end_month, 1)

        if start_date<=current_date1 and current_date2<=end_date:
            # Filter documents based on the year and month range
            docs = collection.find()

            # Initialize order_priority_counts dictionary
            order_priority_counts = {}

            # Extract orderPriority counts from filtered documents
            for doc in docs:
                if 'order_priority_counts' in doc:
                    counts = json.loads(doc['order_priority_counts'])
                    for key, value in counts.items():
                        # Parse year, month, and orderPriority from the key
                        key = key.strip("()").replace("'", "").split(", ")
                        year = int(key[0])
                        month = int(key[1])
                        orderPriority = key[2]
                        # Check if the year and month are within the range
                        if current_date1 <= datetime(year, month, 1) <= current_date2:
                            # Add the count to the corresponding orderPriority
                            if orderPriority in order_priority_counts:
                                order_priority_counts[orderPriority] += value
                            else:
                                order_priority_counts[orderPriority] = value
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