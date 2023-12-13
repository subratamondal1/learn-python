class Employee:
    def __init__(self, name:str, salary:float) -> None:
        self.name = name
        self.salary = salary

    def raise_salary(self, factor):
        return self.salary * factor