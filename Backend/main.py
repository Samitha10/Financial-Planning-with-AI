import logging
from fastapi import APIRouter, BackgroundTasks, FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from dotenv import load_dotenv
from auth.handler import signJWT
from cryptography.fernet import Fernet
import os

from routes.Automate import AutomateRoute
from routes.Charts.valueCounts import valueCountsRoute    
from routes.Charts.Sales import SalesRoute 
from routes.Forecast import ForecastRoute

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.include_router(AutomateRoute,
    prefix="/Automate",
    tags=["Automate"],)

app.include_router(valueCountsRoute, prefix="/ValueCounts", tags=["Froute - ValueCounts"])
app.include_router(SalesRoute, prefix="/Sales", tags=["Froute - Sales"])
app.include_router(ForecastRoute, prefix="/Forecast", tags=["Froute - Forecast"])


# React app is running on port 3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=[("http://localhost:3000")],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
# Vite app is running on port 5173
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


load_dotenv()  # Load environment variables from .env file

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

from connection import collection2
from fastapi import status

class UserCredentials(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    message: str

@app.post('/token', tags=["authentication"], response_model=LoginResponse)
async def login(credentials: UserCredentials):
    UN = credentials.username
    PW = credentials.password
    user_dict = collection2.find_one({"username": UN})
    if user_dict and user_dict.get("password") == PW:
        access_token = signJWT(user_dict["username"])
        return LoginResponse(access_token=access_token, token_type="bearer", message="Login successful")
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    

from cryptography.fernet import Fernet   
with open("Fkey.key", "rb") as key_file:
    Fkey = key_file.read()
cipher_suite = Fernet(Fkey)

@app.post('/tokencheck', tags=["authentication"], response_model=LoginResponse)
async def login(credentials: UserCredentials):
    try:
        UN = credentials.username
        user_dict = collection2.find_one({"username": UN})
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Invalid Username"
        )
    
    decrypted_password_bytes = cipher_suite.decrypt(user_dict["password"])
    decrypted_password = decrypted_password_bytes.decode('utf-8')
    PW = decrypted_password

    if PW == credentials.password:
        access_token = signJWT(user_dict["username"])
        return LoginResponse(access_token=access_token, token_type="bearer", message="Login successful")
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
            headers={"WWW-Authenticate": "Bearer"},
        )


@app.post('/register', tags=["authentication"])
async def register(credentials: UserCredentials):
    existing_user = collection2.find_one({"username": credentials.username})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
        )
    else:
        password_bytes = bytes(credentials.password, 'utf-8')
        encrypted_password = cipher_suite.encrypt(password_bytes)
        collection2.insert_one({"username": credentials.username, "password": encrypted_password})
        decrypted_password_bytes = cipher_suite.decrypt(encrypted_password)
        decrypted_password = decrypted_password_bytes.decode('utf-8')
        return {"C":credentials.password, "E":encrypted_password, "D":decrypted_password}