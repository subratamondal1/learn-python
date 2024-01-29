import pydantic
from pydantic import BaseModel

print(pydantic.__version__)

class User(BaseModel):
    id:int
    name:str="Subrata"

user=User(id=1)
print(user.id, user.name, (type(user.id), type(user.name)))
print(user.model_fields_set)


user=User(id=1, name="Suvo")
print(user.id, user.name, (type(user.id), type(user.name)))
print(user.model_fields_set)

user=User(id="123", name="Suvo") # Auto conversion to int dtype
print(user.id, user.name, (type(user.id), type(user.name)))
print(user.model_fields_set)

print(user.model_dump()) # A dictionary representation of the model.
print(user.model_dump_json()) # A JSON string representation of the model.
print(user.model_json_schema()) # The JSON schema for the given model class.