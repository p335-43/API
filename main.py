from fastapi import FastAPI
app= FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World!!"}

@app.get("/about")
def about():
    return {'message':'this is the about section'}


@app.get("/get_User")
def get_users():
    return [
        {"id":1,"name":"pranjal"},
        {"id":2,"name":"bhavna"}
    ]
    
# getting the data from the parameterised function 

@app.get("/users/{user_id}")
def get_user(user_id:int):
    return {
        "user_id":user_id,
        "message":"user found"
    }
# This is one of the major advantages of FastAPI: Python type hints are used for validation and API documentation.


# Multiple Path Parameters

@app.get("/users/{user_id}/order/{order_id}")
def get_order(user_id:int,order_id:int):
    return{
        "user_id":user_id,
        "order_id":order_id,
        'message':'both are found'
    }

#Query Parameter

@app.get("/userr")
def get_user(age:int):
    return {
        "age":age
    }
    
# if we don't require the value we can give it a default value 
# example:-
@app.get("/userrs")
def get_user(age:int=78):
    return {
        "age":age
    }

# multiple query parameters 
@app.get("/info")
def gte_info(user_id:int, city:str,name:str):
    return [
        {"user_id":user_id},
        {"city":city,'name':name}
    ]
    
# we can also make something optional like 

from typing import Optional

@app.get("/getting_user")
def getuser(age:Optional[int]=None):
    return {
        "age":age
    }
    
#combining the path and query paramethers

@app.get("/product/{product_id}")
def user(product_id:int,
        quantity:int=90,
        discount:Optional[int]=0):
    return {
        "product_id":product_id,
        "quantity":quantity,
        "discount":discount
    }