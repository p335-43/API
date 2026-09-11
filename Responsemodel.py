from pydantic import BaseModel
from fastapi import FastAPI
from typing import Optional

#creating a response model 


app=FastAPI()

class User(BaseModel):   # the data we receive 
    name:str
    age:int
    email:str
    password:str
    
class Userresponse(BaseModel):# the data we are allowed to send back 
    id:int
    name:str
    age:int
    email:Optional[str]=None


@app.post("/users",response_model=Userresponse)
def create_user(user:User):
    print(user)
    return user


@app.get("/resp",response_model=Userresponse)
def user_response():
    return {
        "name":"pranjal",
        "age":23
    }
    

@app.post("/post",response_model=Userresponse)
def create_user(user:User):
    new_user={
        "id":1,
        "name":user.name,
        "age":user.age,
        "email":user.email,
        "password":user.password
    }
    
    print(new_user)
    
    return new_user

# multiple response 

from typing import List

@app.get("/get_data",response_model=list[Userresponse])
def getting_data(user:User):
    return[
        {
            "id":1,
            "name":user.name,
            "age":user.age,
            "email":user.email,
            "password":user.password
        },
        {
            
            "id":2,
            "name":user.name,
            "age":user.age,
            "email":user.email,
            "password":user.password
                    
        },
    ]