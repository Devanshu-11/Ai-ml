from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI();

# Pydantic-It is a python library used for data validation,type checking,and converting data into the expected format
class User(BaseModel):
    name:str
    age:int

@app.post("/create-user")
def create_user(name:str,age:int):
    return{
        "name":name,
        "age":age
    }

@app.post("/create_user_again")
def create_user_again(user:User):
    return{
        "message":"User created successfully",
        "data":user
    }