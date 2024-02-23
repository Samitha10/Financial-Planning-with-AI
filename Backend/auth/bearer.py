from fastapi import Request, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
from dotenv import load_dotenv
import os

load_dotenv()

class JWTBearer(OAuth2PasswordBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        authorization: str = request.headers.get("Authorization")
        scheme, param = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(status_code=403, detail="Invalid scheme")
        return self.verify_jwt(param)

    def verify_jwt(self, jwtoken: str):
        try:
            payload = jwt.decode(jwtoken, os.getenv("SECRET_KEY"), algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=403, detail="Signature has expired")
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=403, detail="Invalid token")
        return payload