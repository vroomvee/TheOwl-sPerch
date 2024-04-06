
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import databases
import sqlalchemy
from pydantic import BaseModel

DATABASE_URL = "mysql://username:password@localhost/database_name"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# Define a model for your user
class User(BaseModel):
    email: str
    username: str
    password: str

# Define the table schema
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("email", sqlalchemy.String(100)),
    sqlalchemy.Column("username", sqlalchemy.String(100)),
    sqlalchemy.Column("password", sqlalchemy.String(100)),
)

# Create the FastAPI app
app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/login")
async def login(user: User):
    query = users.select().where(users.c.email == user.email and users.c.username == user.username and users.c.password == user.password)
    user_data = await database.fetch_one(query)
    if user_data is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful"}
