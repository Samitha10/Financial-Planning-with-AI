import time
import jwt
from decouple import config 


JWT_SECRET = config('JWT_SECRET')
JWT_ALGORITHM = config('JWT_ALGORITHM')

# Function to encode a token
def token_response(token:str):
    return {
        "access_token": token
    }
# Function to sign a token
def signJWT(user_id: str):
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)
# Function to decode a token
def decodeJWT(token:str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decode_token if decode_token['expires'] >= time.time() else 'Token expired'
    except:
        return 'Invalid token'