from uuid import uuid4
from pydantic import BaseModel, Field

class User(BaseModel):
    name:str=Field(default="Subrata Mondal")

user=User()
print(user)
print(user.model_dump())

###############Unique Id###############################
class User(BaseModel):
    id:str=Field(default_factory=lambda: uuid4().hex)

user=User()
print(user)
print(user.model_dump())

##############Alias################################
class User(BaseModel):
    name:str=Field(default=..., alias="username")

user=User(username="Subrata Mondal")
print(user)
print(user.model_dump(by_alias=False))
