from typing import List
from pydantic import BaseModel, EmailStr, PositiveInt, conlist, Field, HttpUrl

class Address(BaseModel):
    street:str
    city:str
    state:str
    zip_code:str

class Employee(BaseModel):
    name:str
    position:str
    email:EmailStr

class Owner(BaseModel):
    name:str
    email:EmailStr

class Restaurant(BaseModel):
    name:str=Field(default=..., pattern=r"^[a-zA-Z0-9-' ]+$") 
    owner:Owner 
    address:Address
    employees:conlist(item_type=Employee, min_length=2)
    number_of_seats:PositiveInt
    delivery:bool
    website:HttpUrl

restaurant=Restaurant(
    name="Tasty Bytes",
    owner={
        "name":"Subrata Mondal",
        "email":"subratasubha2@gmail.com"
    },
    address={
        "street": "Dastamara Road, Murshidabad",
        "city":"Jangipur",
        "state":"West Bengal",
        "zip_code":"742213"
    },
    employees=[
        {"name":"Suvo", "position":"ML Engineer", "email":"subratasubha2@gmail.com"},
        {"name":"Shlok", "position":"ML Engineer", "email":"connect.shlokjain@gmail.com"}
    ],
    number_of_seats=50,
    delivery=True,
    website="https://tastybites.com"
)

print(restaurant)
print(restaurant.model_dump())




