from fastapi import FastAPI, Body, HTTPException, APIRouter,Depends
import pymongo, traceback
from pymongo.mongo_client import MongoClient
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

from auth.model import PostSchema, UserSchema, UserLoginSchema
from auth.jwt_handler import signJWT
from auth.jwt_bearer import jwtBearer

from routes.Automate import AutomateRoute
from routes.Charts.valueCounts import valueCountsRoute    
from routes.Charts.Sales import SalesRoute 

app = FastAPI()
app.include_router(AutomateRoute, prefix="/Automate", tags=["Automate"])
app.include_router(valueCountsRoute, prefix="/ValueCounts", tags=["Froute - ValueCounts"])
app.include_router(SalesRoute, prefix="/Sales", tags=["Froute - Sales"])

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


Posts = [
    {
        'id': 1,
        'title': 'First Post',
        'content': 'This is the content of the first post'
    },
    { 
        'id': 2,
        'title': 'Second Post',
        'content': 'This is the content of the second post'
    },
    {
        'id': 3,
        'title': 'Third Post',
        'content': 'This is the content of the third post'
    }
]

users = []


# Get all the posts
@app.get('/Posts', tags=["Posts"])
def get_posts():
    return {'data': Posts}

# Get a single post
@app.get('/Posts/{id}', tags=["Posts"])
def get_one_post(id: int):
    if id>len(Posts):
        return {"message":"Post not found"}
    for post in Posts:
        if post['id'] == id:
            return {'data': post}
        
# Add a new post
@app.post('/Posts', dependencies=[Depends(jwtBearer())],tags=["Posts"])
def add_post(post: PostSchema):
    post.id = len(Posts) + 1
    Posts.append(post)
    return {'data': 'Posts added successfully'}

# User Sign Up
@app.post('/user_signup', tags=["User"])
def user_signup(user: UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)

def check_user(data: UserLoginSchema):
    for user in users:
        if (user.email == data.email) and (user.password == data.password):
            return True
    return False

@app.post('/user_login', tags=["User"])
def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")