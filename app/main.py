from enum import auto
from typing import Optional, List
from fastapi import  FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from requests import delete
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware


#models.Base.metadata.create_all(bind=engine)

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#while True:

   # try:
        #conn = psycopg2.connect(host='localhost', database='fastboy', user='postgres',
        #password='eternity', cursor_factory=RealDictCursor)
        #cursor = conn.cursor()
        #print('Database connection was succssfull')
        #break
    #except Exception as error:
        #print('connecting to database failed')
        #print('Error was:' , error )
        #time.sleep(2)



app.include_router(auth.router)
app.include_router(post.router)
app.include_router(user.router)
app.include_router(vote.router)



@app.get("/")
def read_root():
    return {"Hello": "sup dude??"}



