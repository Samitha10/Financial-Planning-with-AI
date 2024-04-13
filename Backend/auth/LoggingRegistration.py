import os
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr, Field
from auth.handler import signJWT
from fastapi import APIRouter, HTTPException
LoginRegistrationRoute = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
load_dotenv()  # Load environment variables from .env file

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

from connection import collection2
from fastapi import HTTPException, status
from auth.model import UserSchemaIn, UserLoginSchemaOut, UserSchemaReg


# Load the Fernet key from the file
from cryptography.fernet import Fernet   
with open("auth/Fkey.key", "rb") as key_file:
    Fkey = key_file.read()
cipher_suite = Fernet(Fkey)

# User Authentication
@LoginRegistrationRoute.post('/UserValidation', response_model=UserLoginSchemaOut)
async def login(credentials: UserSchemaIn):
    try:
        UN = credentials.email
        user_dict = collection2.find_one({"email": UN})
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Invalid Username"
        )
    
    decrypted_password_bytes = cipher_suite.decrypt(user_dict["password"])
    decrypted_password = decrypted_password_bytes.decode('utf-8')
    PW = decrypted_password

    if PW == credentials.password:
        access_token = signJWT(user_dict["email"])
        return UserLoginSchemaOut(access_token=access_token, token_type="bearer", message="Login successful")
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
            headers={"WWW-Authenticate": "Bearer"},
        )

# User Registration
@LoginRegistrationRoute.post('/UserRegistration')
async def register(credentials: UserSchemaReg):
    existing_user = collection2.find_one({"email": credentials.email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
        )
    else:
        password_bytes = bytes(credentials.password, 'utf-8')
        encrypted_password = cipher_suite.encrypt(password_bytes)
        collection2.insert_one({"username":credentials.username, "email": credentials.email, "password": encrypted_password})
        return {"message": "User registered successfully"}
        # decrypted_password_bytes = cipher_suite.decrypt(encrypted_password)
        # decrypted_password = decrypted_password_bytes.decode('utf-8')
        # return {"C":credentials.password, "E":encrypted_password, "D":decrypted_password}