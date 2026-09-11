from fastapi import FastAPI, HTTPException,status
from pydantic import BaseModel

app=FastAPI()

users = {
    1: "Pranjal",
    2: "Rahul",
    3: "Amit"
}


@app.get("/users/{user_id}")
def get_user(user_id:int):
    
    if user_id not in users:
        raise HTTPException(
            # status_code=404, --> this is also correct but we cal also use 
            status_code=status.HTTP_404_NOT_FOUND,
            detail='user not found with this user id'
        )
    return {
        "id":user_id,
        "name":users[user_id]
    }


# another  example 

@app.post("/verification")
def verify(age:int):
    if age<18:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="user must be greater than 18 years"
        )
        
    return{
        "age":age,
        "detail":"you are allowed to proceed within the website"
    }


# validation error 

@app.get("/finduser/{user_id}")
def find_user(user_id:int):
    if not isinstance(user_id,int):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="user id must be an integer"
        )
    return{
        "id":user_id,
        "detail":"user found with this id"
    }

# real life example 

class Usercreate(BaseModel):
    name:str
    age:int

class UserResponse(BaseModel):
    id:int
    name:str
    age:int
    
userrs={}

@app.post("/create_user",response_model=UserResponse,status_code=status.HTTP_201_CREATED)
def create_user(user:Usercreate):
    user_id=len(userrs)+1
    
    new_user={
        "id":user_id,
        "name":user.name,
        "age":user.age
    }
    
    userrs[user_id]=new_user
    
    return new_user

@app.get(
    "/userrs/{user_id}",
    response_model=UserResponse
)
def get_user(user_id: int):

    if user_id not in userrs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return userrs[user_id]
