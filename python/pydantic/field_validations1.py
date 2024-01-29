from pydantic import BaseModel, EmailStr, field_validator

class Owner(BaseModel):
    name:str
    email:EmailStr

    @field_validator('name')
    @classmethod
    def name_must_contain_space(cls, v:str) -> str:
        if " " not in v:
            raise ValueError("Owner name must contain a space")
        return v.title()
try:
    owner=Owner(name="Subrata Mondal", email="subratasubha2@gmail.com")
    print(owner)
    print(owner.model_dump())
except ValueError as e:
    print(e)
