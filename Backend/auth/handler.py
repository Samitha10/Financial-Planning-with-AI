import jwt
import time
from dotenv import load_dotenv
import os

load_dotenv()

def signJWT(username: str):
    payload = {
        'username': username,
        'expiry': time.time() + 600
    }
    token = jwt.encode(payload, os.getenv("SECRET_KEY"), algorithm="HS256")
    return token