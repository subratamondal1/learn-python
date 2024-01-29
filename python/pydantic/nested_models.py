from pydantic import BaseModel
from typing import List, Optional

class Food(BaseModel):
    name:str
    price:float
    ingredients:Optional[List[str]]=None

class Restaurant(BaseModel):
    name:str
    location:str
    foods:List[Food]

restaurant=Restaurant(
    name="Tasty Bites",
    location="Jangipur, Murshidabad",
    foods=[
        {"name":"Cheese Burger", "price": 50.00},
        {"name":"Chicken Biryani", "price": 180.00, "ingredients":["Masala", "Chicken", "Rice"]},
    ]
)

print(restaurant)
print(restaurant.model_dump())

