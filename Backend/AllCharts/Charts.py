from fastapi import FastAPI, APIRouter
import pandas as pd

router1 = APIRouter()

@router1.get('/test1')
def test1():
    df1 = pd.read_csv('fullData.csv')
    data1 = df1['ship_mode'].value_counts().to_dict()
    return {"data": data1}

