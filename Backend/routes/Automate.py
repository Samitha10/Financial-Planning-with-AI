from fastapi import APIRouter, HTTPException
AutomateRoute = APIRouter()

from connection import data, collection

@AutomateRoute.post('/valueCounts_shipMode')
def valueCounts_shipMode():
    try:
        grouped_data = data.groupby(['year', 'month', 'ship_mode'])
        data1 = grouped_data['ship_mode'].count().to_json()
        # Delete all documents that have the key "ship_mode_counts"
        collection.delete_many({"ship_mode_counts": {"$exists": True}})
        # Insert the new document
        collection.insert_one({"ship_mode_counts": data1})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/valueCounts_segment')
def valueCounts_segment():
    try:
        grouped_data = data.groupby(['year', 'month', 'segment'])
        data2 = grouped_data['segment'].count().to_json()
        # Delete all documents that have the key "segment_counts"
        collection.delete_many({"segment_counts": {"$exists": True}})
        # Insert the new document
        collection.insert_one({"segment_counts": data2})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/valueCounts_state')
def valueCounts_state():
    try:
        grouped_data = data.groupby(['year', 'month', 'state'])
        data3 = grouped_data['state'].count().to_json()
        # Delete all documents that have the key "state_counts"
        collection.delete_many({"state_counts": {"$exists": True}})
        # Insert the new document
        collection.insert_one({"state_counts": data3})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/valueCounts_country')
def valueCounts_country():
    try:
        grouped_data = data.groupby(['year', 'month', 'country'])
        data4 = grouped_data['country'].count().to_json()
        # Delete all documents that have the key "country_counts"
        collection.delete_many({"country_counts": {"$exists": True}})
        # Insert the new document
        collection.insert_one({"country_counts": data4})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/valueCounts_market')
def valueCounts_market():
    try:
        grouped_data = data.groupby(['year', 'month', 'market'])
        data5 = grouped_data['market'].count().to_json()
        data5 = data['market'].value_counts().to_json()
        # Delete all documents that have the key "market_counts"
        collection.delete_many({"market_counts": {"$exists": True}})
        # Insert the new document
        collection.insert_one({"market_counts": data5})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/valueCounts_region')
def valueCounts_region():
    try:
        grouped_data = data.groupby(['year', 'month', 'region'])
        data6 = grouped_data['region'].count().to_json()
        # Delete all documents that have the key "region_counts"
        collection.delete_many({"region_counts": {"$exists": True}})
        # Insert the new document
        collection.insert_one({"region_counts": data6})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/valueCounts_category')
def valueCounts_category():
    try:
        grouped_data = data.groupby(['year', 'month', 'category'])
        data7 = grouped_data['category'].count().to_json()
        # Delete all documents that have the key "category_counts"
        collection.delete_many({"category_counts": {"$exists": True}})
        # Insert the new document
        collection.insert_one({"category_counts": data7})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/valueCounts_subCategory')
def valueCounts_subCategory():
    try:
        grouped_data = data.groupby(['year', 'month', 'sub_category'])
        data8 = grouped_data['sub_category'].count().to_json()
        # Delete all documents that have the key "sub_category_counts"
        collection.delete_many({"sub_category_counts": {"$exists": True}})
        # Insert the new document
        collection.insert_one({"sub_category_counts": data8})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/valueCounts_orderPriority')
def valueCounts_orderPriority():
    try:
        grouped_data = data.groupby(['year', 'month', 'order_priority'])
        data9 = grouped_data['order_priority'].count().to_json()
        # Delete all documents that have the key "order_priority_counts"
        collection.delete_many({"order_priority_counts": {"$exists": True}})
        # Insert the new document
        collection.insert_one({"order_priority_counts": data9})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

## Sales and Profit Dashboard
@AutomateRoute.post('/YMSales')
def Sales():
    try:
        
        data10 = data.groupby(['year', 'month']).agg({'sales': 'sum'}).reset_index().to_json()
        # Delete all documents that have the key "sales"
        collection.delete_many({"YMsales": {"$exists": True}})
        # Insert the new document
        collection.insert_one({"YMsales": data10})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/YMProfit')
def Profit():
    try:
        data11 = data.groupby(['year', 'month']).agg({'profit': 'sum'}).reset_index().to_json()
        # Delete all documents that have the key "profit"
        collection.delete_many({"YMprofit": {"$exists": True}})
        # Insert the new document
        collection.insert_one({"YMprofit": data11})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}


# Customer and Product_id Counts
@AutomateRoute.post('/CustomerCounts')
def CustomerCounts():
    try:
        data12 = data['customer_name'].nunique().to_json()
        # Delete all documents that have the key "customer_id_counts"
        collection.delete_many({"Customer_id_counts": {"$exists": True}})
        # Insert the new document
        collection.insert_one({"Customer_id_counts": data12})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/Product_idCounts')
def Product_idCounts():
    try:
        data13 = data.shape[0].to_json()
        # Delete all documents that have the key "product_id_counts"
        collection.delete_many({"Product_id_counts": {"$exists": True}})
        # Insert the new document
        collection.insert_one({"Product_id_counts": data13})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}