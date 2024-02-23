from fastapi import APIRouter, BackgroundTasks, FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from dotenv import load_dotenv
from auth.handler import signJWT
import os

from routes.Automate import AutomateRoute
from routes.Charts.valueCounts import valueCountsRoute    
from routes.Charts.Sales import SalesRoute 
from routes.Forecast import ForecastRoute

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.include_router(AutomateRoute,
    prefix="/Automate",
    tags=["Automate"],
    dependencies=[Depends(oauth2_scheme)],
    responses={404: {"description": "Not found"}})

app.include_router(valueCountsRoute, prefix="/ValueCounts", tags=["Froute - ValueCounts"])
app.include_router(SalesRoute, prefix="/Sales", tags=["Froute - Sales"])
app.include_router(ForecastRoute, prefix="/Forecast", tags=["Froute - Forecast"])

origins = [
    repr("http://localhost:3000"),  # React app address
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()  # Load environment variables from .env file

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

from connection import client,collection2

class User(BaseModel):
    Username: str
    Password: str



@app.on_event("shutdown")
async def shutdown_event():
    client.close()

@app.post('/token', tags=["authentication"])
async def login(background_tasks: BackgroundTasks, form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = collection2.find_one({"Username": form_data.username})
    if user_dict and user_dict["Password"] == form_data.password:
        user = User(**user_dict)
        return {"access_token": signJWT(user.Username), "token_type": "bearer"}
    else:
        raise HTTPException(status_code=400, detail="Invalid credentials")
