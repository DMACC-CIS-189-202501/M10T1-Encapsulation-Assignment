import pytest
import ast
import importlib

# Test to check for file docstring
def test_file_docstring():
    with open('assignment.py', 'r') as file:
        tree = ast.parse(file.read())
    docstring = ast.get_docstring(tree)
    assert docstring is not None, "DMACC Student, there does not appear to be a docstring at the top of your file. Please add a docstring explaining what your code does."

# Test to check if Employee object is created correctly and display method works
def test_employee_display():
    from assignment import Employee
    employee = Employee("Doe", "John", "123 Main St", "555-555-5555", 50000.0, "2023-01-01")
    expected_display = (
        "LAST_NAME, FIRST_NAME: Doe, John\n"
        "PHONE_NUMBER: 555-555-5555\n"
        "ADDRESS: 123 Main St\n"
        "START DATE: 2023-01-01\n"
        "SALARY: 50000.0\n"
    )
    assert employee.display() == expected_display, f"DMACC Student, the 'display' method did not return the expected string.\nExpected: {expected_display}\nActual: {employee.display()}\nPlease check your display method logic."

# Test to check if last_name attribute exists and is set correctly
def test_employee_last_name():
    from assignment import Employee
    employee = Employee("Doe", "John", "123 Main St", "555-555-5555", 50000.0, "2023-01-01")
    assert hasattr(employee, 'last_name'), "DMACC Student, the 'last_name' attribute does not exist on the Employee object. Please ensure it is set correctly."
    assert employee.last_name == "Doe", f"DMACC Student, the 'last_name' attribute is not set correctly.\nExpected: 'Doe'\nActual: '{employee.last_name}'"

# Test to check if first_name attribute exists and is set correctly
def test_employee_first_name():
    from assignment import Employee
    employee = Employee("Doe", "John", "123 Main St", "555-555-5555", 50000.0, "2023-01-01")
    assert hasattr(employee, 'first_name'), "DMACC Student, the 'first_name' attribute does not exist on the Employee object. Please ensure it is set correctly."
    assert employee.first_name == "John", f"DMACC Student, the 'first_name' attribute is not set correctly.\nExpected: 'John'\nActual: '{employee.first_name}'"

# Test to check if address attribute exists and is set correctly
def test_employee_address():
    from assignment import Employee
    employee = Employee("Doe", "John", "123 Main St", "555-555-5555", 50000.0, "2023-01-01")
    assert hasattr(employee, 'address'), "DMACC Student, the 'address' attribute does not exist on the Employee object. Please ensure it is set correctly."
    assert employee.address == "123 Main St", f"DMACC Student, the 'address' attribute is not set correctly.\nExpected: '123 Main St'\nActual: '{employee.address}'"

# Test to check if phone_number attribute exists and is set correctly
def test_employee_phone_number():
    from assignment import Employee
    employee = Employee("Doe", "John", "123 Main St", "555-555-5555", 50000.0, "2023-01-01")
    assert hasattr(employee, 'phone_number'), "DMACC Student, the 'phone_number' attribute does not exist on the Employee object. Please ensure it is set correctly."
    assert employee.phone_number == "555-555-5555", f"DMACC Student, the 'phone_number' attribute is not set correctly.\nExpected: '555-555-5555'\nActual: '{employee.phone_number}'"

# Test to check if salary attribute exists and is set correctly
def test_employee_salary():
    from assignment import Employee
    employee = Employee("Doe", "John", "123 Main St", "555-555-5555", 50000.0, "2023-01-01")
    assert hasattr(employee, 'salary'), "DMACC Student, the 'salary' attribute does not exist on the Employee object. Please ensure it is set correctly."
    assert employee.salary == 50000.0, f"DMACC Student, the 'salary' attribute is not set correctly.\nExpected: 50000.0\nActual: {employee.salary}"

# Test to check if start_date attribute exists and is set correctly
def test_employee_start_date():
    from assignment import Employee
    employee = Employee("Doe", "John", "123 Main St", "555-555-5555", 50000.0, "2023-01-01")
    assert hasattr(employee, 'start_date'), "DMACC Student, the 'start_date' attribute does not exist on the Employee object. Please ensure it is set correctly."
    assert employee.start_date == "2023-01-01", f"DMACC Student, the 'start_date' attribute is not set correctly.\nExpected: '2023-01-01'\nActual: '{employee.start_date}'"

if __name__ == "__main__":
    pytest.main()