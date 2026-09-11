#sending data from the fastapi 
from fastapi import Body, FastAPI
from pydantic import BaseModel
from typing import Optional



app= FastAPI()


class User(BaseModel):
    name:str
    age:int
    email:Optional[str]=None


@app.post("/users")
def create_user(user:User): #The user parameter should contain data matching the User Pydantic model.
    return user
# the above means this are present inside the function 
#user.name
# user.age
# user.email

# proving the above concept 

@app.post("/user_info")
def create_user(user:User):
    return {
        "message":f"hello {user.name}",
        "age":user.age,
        "mail":user.email
    }
    
#path +body + query together 

class Product(BaseModel):
    name:str
    price:float


@app.put("/product/{product_id}")
def update_product(
    product_id:int,
    product:Product,
    discount:int=0
):
    return{
        "name":product.name, #--> request body
        "price":product.price,
        "product_id":product_id, # path parameter
        "discount":discount #query parameter
    }


@app.post("/create_post")
def create_post(info:dict=Body(...)):
    print(info)
    return {'message':'successfully created post'}


# nested pydantic models 

class Address(BaseModel):
    city:str
    pincode:int

class Persom(BaseModel):
    name:str
    age:int
    address:Address

@app.post("/students")
def student_info(
    person:Persom
):
    return {
        "person name ":person.name,
        "person age":person.age,
        "person address":{
            "city":person.address.city,
            "pincode":person.address.pincode
        }
    }