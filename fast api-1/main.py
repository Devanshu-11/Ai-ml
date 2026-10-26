from fastapi import FastAPI

# creates an instance of the FastAPI class
app=FastAPI();

# Home Route
@app.get("/")
# Def is a keyword used to define a function and inside it,i have taken no arguments into it
def home(): 
    return{"message":"Hello without virtual environment"};

# About route
@app.get("/about")
def about():
    return{"message":"This is about page"};

# Users route
@app.get("/users")
def users():
    return{
        "users":["Mohit","Rohit","Amit"]
    };

# Path Parameters-If we want to change the dynamic value of url path like-/orders/1 and /orders/2 for different orders items
@app.get("/orders/{order_id}")
def get_orders(order_id:int):
    return {"Order is: ":order_id};

# Query Parameters-These are used after a ? which is commonly used for Searching,Sorting,Pagination and filtering, eg-/products?price=1000 in which we filter the products based on price equals to 1000
# optional Parameters
@app.get("/products")
def get_products(name:str|None=None):
    return{"Name: ":name};

# Default Parameters
@app.get("/product-limit")
def get_product_name(limit:int=10):
    return{"Limit: ":limit};

# Multiple Query Parameters
@app.get("/items")
def get_items(name:str=None,price:int=0):
    return{"Name is: ":name,"Price is: ":price};