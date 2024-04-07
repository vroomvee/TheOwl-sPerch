from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app=FastAPI()
models.Base.metadata.create_all(bind=engine)

class EmpBase(BaseModel):
    eusername:str
    epwd:str
    eemailid:str
    eid:int

class UserBase(BaseModel):
    username:str
    pwd:str
    emailid:str
    id:int

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency=Annotated[Session,Depends(get_db)]

@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user:UserBase,db:db_dependency):
    db_user=models.User(**user.dict())
    db.add(user)
    db.commit(