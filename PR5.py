print("--- Python OOP Project: Employee Management System --- ")

print("Choose an option")
print("1. Create a Person")
print("2. Create an Employee")
print("3. Create a Manager")
print("4. Show Details")
print("5. Compare Salaries")
print("6. Exit")

while True:

    choice = int(input("Enter your choice: "))

    if choice == 1:
        person_name = input("Enter Name: ")
        person_age = input("Enter Age: ")

        class Person:

            def __init__(self, name, age):
                self.name = name
                self.age = age

            def display(self):
                print(f"Person name is {self.name} and age is {self.age}")

        p1 = Person(person_name, person_age)
        p1.display()

    elif choice == 2:
        employee_salary = int(input("Enter Salary: "))
        employee_id = int(input("Enter ID: "))

        class Employee(Person):

            def __del__(self):
                print(f"Employee name {self.name} is Destroyed")

            def set_id_salary(self, id, salary):
                self.id = id
                self.salary = salary

            def get_id_salary(self):
                return self.id, self.salary, self.name, self.age

        Emp1 = Employee(employee_salary, employee_id)
        Emp1.set_id_salary(1, 25000)
        print(Emp1.get_id_salary())
