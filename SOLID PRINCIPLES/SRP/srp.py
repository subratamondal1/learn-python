### SINGLE RESPONSIBILITY PRINCIPLE ###

from employee import Employee
from employee_storage import EmployeeDB

employee1 = Employee(
    name="Subrata Mondal",
    salary=50000.00
)

store = EmployeeDB()

store.save_employee(
    employee=employee1
)