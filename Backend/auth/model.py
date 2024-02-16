from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id : int = Field(default=None,alias='_id')
    title : str = Field(default=None)
    content : str = Field(default=None)
    class Config:
        json_schema_extra = {
            "post_demo": {
                "title": "Example Title",
                "content":"This is an example content"
            }
        }

class UserSchema(BaseModel):
    username : str = Field(default=None)
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    class Config:
        json_schema_extra = {
            "user_demo": {
                "username": "Username1",
                "email":"example@mail.com",
                "password":"123"
            }
        }

class UserLoginSchema(BaseModel):
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    class Config:
        json_schema_extra = {
            "user_demo": {
                "email":"example@mail.com",
                "password":"123"
            }
        }