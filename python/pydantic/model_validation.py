from typing import Any 
from pydantic import BaseModel, EmailStr, ValidationError, model_validator

class Owner(BaseModel):
    name:str
    email:EmailStr

    @model_validator(mode="before")
    @classmethod
    def check_sensitive_info_omitted(cls, data:Any) -> Any:
        if isinstance(data, dict):
            if "password" in data:
                raise ValueError("Password should not be included")
            if "card_number" in data:
                raise ValueError("Card Number should not be included")
        return data
    
    @model_validator(mode="after")
    def check_name_contains_space(self) -> 'Owner':
        if " " not in self.name:
            raise ValueError("Owner name must contain a space")
        return self

try:
    owner=Owner(name="Subrata Mondal", email="subratasubha2@gmail.com")
    print(owner)
    print(owner.model_dump())

except ValidationError as e:
    print(e)
