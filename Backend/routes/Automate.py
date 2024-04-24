from fastapi import APIRouter, HTTPException
import pymongo
AutomateRoute = APIRouter()

from connection import data, collection, collection4, collection5, MONGO_URI
negData = data[data['profit'] < 0]

current_data_count = 51287

def Datacount():
    try:
        # Connect to the MongoDB server
        client = pymongo.MongoClient(MONGO_URI)
        db = client.get_database()

        COLLECTION_NAME1 = "Super_Store_Data"
        collection = db[COLLECTION_NAME1]

        # Count the number of documents in the collection
        count = collection.count_documents({})

        return count

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@AutomateRoute.get('/Datacount')
def datacount():
    return {'data_count': Datacount()}

# Checking wheather the data is added or deleted from the MongoDB
def check_count():
    global current_data_count
    if current_data_count == Datacount():
        return True
    else:
        current_data_count = Datacount()
        return {'Data is being updated',current_data_count}


@AutomateRoute.get('/check_count')
def get_check_count():
    return check_count()


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


# Top 20s----------------------------------------------------------------------------
@AutomateRoute.post('/product with the most sales')
def product_with_the_most_sales():
    try:
        data14 = data[['sales','product_name']].groupby('product_name').sum().sort_values('sales',ascending=False).head(10).reset_index().to_json()
        # Delete all documents that have the key "product_with_the_most_sales"
        collection4.delete_many({"product_with_the_most_sales": {"$exists": True}})
        # Insert the new document
        collection4.insert_one({"product_with_the_most_sales": data14})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/product with average sales')
def product_with_average_sales():
    try:
        data15 = data[['sales','product_name']].groupby('product_name').mean().sort_values('sales',ascending=False).head(10).reset_index().to_json()
        # Delete all documents that have the key "product_with_average_sales"
        collection4.delete_many({"product_with_average_sales": {"$exists": True}})
        # Insert the new document
        collection4.insert_one({"product_with_average_sales": data15})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/countries with the most sales')
def countries_with_the_most_sales():
    try:
        data16 = data[['sales','country']].groupby('country').sum().sort_values('sales',ascending=False).head(10).reset_index().to_json()
        # Delete all documents that have the key "countries_with_the_most_sales"
        collection4.delete_many({"countries_with_the_most_sales": {"$exists": True}})
        # Insert the new document
        collection4.insert_one({"countries_with_the_most_sales": data16})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/countries with average sales')
def countries_with_average_sales():
    try:
        data17 = data[['sales','country']].groupby('country').mean().sort_values('sales',ascending=False).head(10).reset_index().to_json()
        # Delete all documents that have the key "countries_with_average_sales"
        collection4.delete_many({"countries_with_average_sales": {"$exists": True}})
        # Insert the new document
        collection4.insert_one({"countries_with_average_sales": data17})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/regions with the most sales')
def regions_with_the_most_sales():
    try:
        data18 = data[['sales','region']].groupby('region').sum().sort_values('sales',ascending=False).head(10).reset_index().to_json()
        # Delete all documents that have the key "regions_with_the_most_sales"
        collection4.delete_many({"regions_with_the_most_sales": {"$exists": True}})
        # Insert the new document
        collection4.insert_one({"regions_with_the_most_sales": data18})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/regions with average sales')
def regions_with_average_sales():
    try:
        data19 = data[['sales','region']].groupby('region').mean().sort_values('sales',ascending=False).head(10).reset_index().to_json()
        # Delete all documents that have the key "regions_with_average_sales"
        collection4.delete_many({"regions_with_average_sales": {"$exists": True}})
        # Insert the new document
        collection4.insert_one({"regions_with_average_sales": data19})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}


### Negative Subset

#Top 20 best selling products in the Negative subset
@AutomateRoute.post('/Negative product with the most sales')
def Negative_Product_with_the_most_sales():
    try:
        data20 = negData[['product_name','sales']].groupby('product_name').sum().sort_values('sales', ascending=False).reset_index().head(10).to_json()
        # Delete all documents that have the key "product_with_the_most_sales_in_the_negative_subset"
        collection5.delete_many({"product_with_the_most_sales": {"$exists": True}})
        # Insert the new document
        collection5.insert_one({"product_with_the_most_sales": data20})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

#Top 20: Average best-selling products in the Negative subset
@AutomateRoute.post('/Negative product with average sales')
def Negative_Product_with_average_sales():
    try:
        data21 = negData[['product_name','sales']].groupby('product_name').mean().sort_values('sales', ascending=False).reset_index().head(10).to_json()
        # Delete all documents that have the key "product_with_average_sales_in_the_negative_subset"
        collection5.delete_many({"product_with_average_sales": {"$exists": True}})
        # Insert the new document
        collection5.insert_one({"product_with_average_sales": data21})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

#Negative ['order_priority','market','region','category','sub_category','ship_mode'] with profit
@AutomateRoute.post('/Negative order priprity with profit')
def Negative_Order_priority_with_profit():
    try:
        data22 = negData[['order_priority','profit']].groupby('order_priority').sum().sort_values('profit', ascending=False).reset_index().to_json()
        # Delete all documents that have the key "order_priority_with_profit"
        collection5.delete_many({"order_priority_with_profit": {"$exists": True}})
        # Insert the new document
        collection5.insert_one({"order_priority_with_profit": data22})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}


@AutomateRoute.post('/Negative market with profit')
def Negative_Market_with_profit():
    try:
        data23 = negData[['market','profit']].groupby('market').sum().sort_values('profit', ascending=False).reset_index().to_json()
        # Delete all documents that have the key "market_with_profit"
        collection5.delete_many({"market_with_profit": {"$exists": True}})
        # Insert the new document
        collection5.insert_one({"market_with_profit": data23})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/Negative region with profit')
def Negative_Region_with_profit():
    try:
        data24 = negData[['region','profit']].groupby('region').sum().sort_values('profit', ascending=False).reset_index().to_json()
        # Delete all documents that have the key "region_with_profit"
        collection5.delete_many({"region_with_profit": {"$exists": True}})
        # Insert the new document
        collection5.insert_one({"region_with_profit": data24})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/Negative category with profit')
def Negative_Category_with_profit():
    try:
        data25 = negData[['category','profit']].groupby('category').sum().sort_values('profit', ascending=False).reset_index().to_json()
        # Delete all documents that have the key "category_with_profit"
        collection5.delete_many({"category_with_profit": {"$exists": True}})
        # Insert the new document
        collection5.insert_one({"category_with_profit": data25})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/Negative sub_category with profit')
def Negative_Sub_category_with_profit():
    try:
        data26 = negData[['sub_category','profit']].groupby('sub_category').sum().sort_values('profit', ascending=False).reset_index().to_json()
        # Delete all documents that have the key "sub_category_with_profit"
        collection5.delete_many({"sub_category_with_profit": {"$exists": True}})
        # Insert the new document
        collection5.insert_one({"sub_category_with_profit": data26})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}

@AutomateRoute.post('/Negative ship_mode with profit')
def Negative_Ship_mode_with_profit():
    try:
        data27 = negData[['ship_mode','profit']].groupby('ship_mode').sum().sort_values('profit', ascending=False).reset_index().to_json()
        # Delete all documents that have the key "ship_mode_with_profit"
        collection5.delete_many({"ship_mode_with_profit": {"$exists": True}})
        # Insert the new document
        collection5.insert_one({"ship_mode_with_profit": data27})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {'message': 'Data inserted into MongoDB successfully.'}