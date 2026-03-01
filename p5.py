
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display(self):
        super().display()
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")



person = None
employee = None
manager = None


while True:
    print("\n----- Python OOP Project : Employee Management System -----")
    print("1. Create Person")
    print("2. Create Employee")
    print("3. Create Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter person's name: ")
        age = int(input("Enter person's age: "))
        person = Person(name, age)
        print("\nPerson Created Successfully!")
        person.display()

    elif choice == 2:
        name = input("Enter employee's name: ")
        age = int(input("Enter employee's age: "))
        employee_id = input("Enter employee ID: ")
        salary = float(input("Enter employee salary: "))
        employee = Employee(name, age, employee_id, salary)
        print("\nEmployee Created Successfully!")
        employee.display()

    elif choice == 3:
        name = input("Enter manager's name: ")
        age = int(input("Enter manager's age: "))
        employee_id = input("Enter manager ID: ")
        salary = float(input("Enter manager salary: "))
        department = input("Enter department: ")
        manager = Manager(name, age, employee_id, salary, department)
        print("\nManager Created Successfully!")
        manager.display()

    elif choice == 4:
        print("\n1. Person Details")
        print("2. Employee Details")
        print("3. Manager Details")
        sub_choice = int(input("Enter your choice: "))

        if sub_choice == 1:
            if person:
                person.display()
            else:
                print("Person not created yet!")

        elif sub_choice == 2:
            if employee:
                employee.display()
            else:
                print("Employee not created yet!")

        elif sub_choice == 3:
            if manager:
                manager.display()
            else:
                print("Manager not created yet!")

        else:
            print("Invalid choice!")

    elif choice == 5:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
