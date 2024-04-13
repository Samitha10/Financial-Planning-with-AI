from pydantic import BaseModel, Field, EmailStr

class UserSchemaIn(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

class UserLoginSchemaOut(BaseModel):
    access_token: str
    token_type: str
    message: str

class UserSchemaReg(BaseModel):
    username : str = Field(default=None)
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
