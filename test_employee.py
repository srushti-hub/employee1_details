#test_employee.py
import pytest
from employee import get_employee_details

def test_get_employee_details():
    #sample data
    name = "Alice Smith"
    emp_id = "E2020"
    department = "HR"
    salary = "60000"
    #Expected result
    expected_output=(
        "Employee Name: Alice Smith\n"
        "Employee ID: E2020\n"
        "Department: HR\n"
        "Salary: 60000"
    )
    #Assertion
    assert get_employee_details(name,emp_id,department,salary) == expected_output
