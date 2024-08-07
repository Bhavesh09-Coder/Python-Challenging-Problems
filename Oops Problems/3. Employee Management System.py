# employee_management.py

# Define a class named 'Employee' to manage employee records.
class Employee:
    def __init__(self, name, position, salary):
        """
        Initialize an Employee object with name, position, and salary.

        :param name: The name of the employee.
        :param position: The position of the employee.
        :param salary: The salary of the employee.
        """
        self.name = name
        self.position = position
        self.salary = salary

    def display_details(self):
        """
        Display the details of the employee.
        """
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary:.2f}")

    def update_position(self, new_position):
        """
        Update the position of the employee.

        :param new_position: The new position of the employee.
        """
        self.position = new_position
        print(f"Position updated to {self.position}")

    def update_salary(self, new_salary):
        """
        Update the salary of the employee.

        :param new_salary: The new salary of the employee.
        """
        self.salary = new_salary
        print(f"Salary updated to ${self.salary:.2f}")

# Define a class named 'EmployeeManagementSystem' to manage a collection of employees.
class EmployeeManagementSystem:
    def __init__(self):
        """
        Initialize an EmployeeManagementSystem object with an empty employee list.
        """
        self.employees = []

    def add_employee(self, employee):
        """
        Add an employee to the system.

        :param employee: The Employee object to be added.
        """
        self.employees.append(employee)
        print(f"Employee {employee.name} added to the system.")

    def remove_employee(self, employee_name):
        """
        Remove an employee from the system by their name.

        :param employee_name: The name of the employee to be removed.
        """
        for employee in self.employees:
            if employee.name == employee_name:
                self.employees.remove(employee)
                print(f"Employee {employee_name} removed from the system.")
                return
        print(f"Employee {employee_name} not found in the system.")

    def display_all_employees(self):
        """
        Display details of all employees in the system.
        """
        if not self.employees:
            print("No employees in the system.")
            return
        for employee in self.employees:
            employee.display_details()
            print("---")

if __name__ == "__main__":
    # Create an instance of EmployeeManagementSystem
    ems = EmployeeManagementSystem()

    # Create a few Employee objects
    emp1 = Employee("Alice", "Developer", 60000)
    emp2 = Employee("Bob", "Designer", 55000)
    emp3 = Employee("Charlie", "Manager", 75000)

    # Add employees to the system
    ems.add_employee(emp1)
    ems.add_employee(emp2)
    ems.add_employee(emp3)

    # Display all employees
    print("\nAll Employees:")
    ems.display_all_employees()

    # Update an employee's position and salary
    emp1.update_position("Senior Developer")
    emp1.update_salary(70000)

    # Display details of a specific employee after update
    print("\nUpdated Details for Alice:")
    emp1.display_details()

    # Remove an employee from the system
    ems.remove_employee("Bob")

    # Display all employees after removal
    print("\nAll Employees After Removal:")
    ems.display_all_employees()
