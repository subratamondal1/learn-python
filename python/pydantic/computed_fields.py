from pydantic import BaseModel, computed_field
from datetime import datetime

class Person(BaseModel):
    name:str
    birth_year:int

    @computed_field
    @property
    def age(self) -> int:
        current_year=datetime.now().year
        return current_year - self.birth_year
    
person=Person(name="Subrata Mondal", birth_year=2000)
print(person)
print(person.age)
print(person.model_dump())