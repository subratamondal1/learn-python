### OPEN CLOSED PRINCIPLE ###
from abc import ABC, abstractmethod

class PersonStorage(ABC):
    @abstractmethod
    def save(self, person:object):
        pass

class PersonDB(PersonStorage):
    def save(self, person: object):
        print(f"Person:{person.name} saved to Database.")

class PersonJSON(PersonStorage):
    def save(self, person: object):
        print(f"Person: {person.name} saved to JSON.")

class PersonXML(PersonStorage):
    def save(self, person: object):
        print(f"Person: {person.name} saved to XML.")

class Person:
    def __init__(self, name) -> None:
        self.name = name

def save_person(storage:object, person:object):
    storage.save(person)

if __name__ == "__main__":
    person = Person(
        name="Subrata Mondal"
    )

    db_storage = PersonDB()
    json_storage = PersonJSON()
    xml_storage = PersonXML()

    save_person(
        storage=db_storage,
        person=person
    )

    save_person(
        storage=json_storage,
        person=person
    )

    save_person(
        storage=xml_storage,
        person=person
    )


