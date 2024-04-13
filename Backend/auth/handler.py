import jwt
import time
from dotenv import load_dotenv
import os

load_dotenv()

def signJWT(email: str):
    payload = {
        'email': email,
        'expiry': time.time() + 600
    }
    token = jwt.encode(payload, os.getenv("SECRET_KEY"), algorithm="HS256")
    return token