from fastapi import FastAPI, APIRouter
import pandas as pd

router2 = APIRouter()

@router2.get('/test2')
def test2():
    df1 = pd.read_csv('fullData.csv')
    data2 = df1['market'].value_counts().to_dict()
    return {"data": data2}
