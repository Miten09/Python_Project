print("Python OOP Project: Employee Management System")

print("Choose an option")
print("1. Create a Person")
print("2. Create an Employee")
print("3. Create a Manager")
print("4. Show Details")
print("5. Compare Salaries")
print("6. Exit")

Emp1 = None
m1 = None
d1 = None
p1 = None

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

        name = input("Employee Name: ")
        age = input("Employee Age: ")
        salary = int(input("Enter Salary: "))
        id = input("Enter ID: ")

        class Employee(Person):

            def __init__(self, name, age, salary=0, id=None):
                super().__init__(name, age)
                self.salary = salary
                self.id = id

            def __del__(self):
                print(f"Employee name {self.name} is Destroyed")

            def set_id_salary(self, id, salary):
                self.id = id
                self.salary = salary

            def get_id_salary(self):
                return f"Employee ID is {self.id} and Salary is {self.salary}, Name is {self.name} and Age is {self.age}"

            def __gt__(self, other):
                return self.salary > other.salary

            def __lt__(self, other):
                return self.salary < other.salary

            def __eq__(self, other):
                return self.salary == other.salary

        Emp1 = Employee(name, age)
        Emp1.set_id_salary(id, salary)

        print(Emp1.get_id_salary())

    elif choice == 3:

        name = input("Employee Name: ")
        age = input("Employee Age: ")
        salary = int(input("Enter Salary: "))
        id = input("Enter ID: ")
        department = input("Enter Department: ")

        class Manager(Employee):

            def __init__(self, name, age, salary, id, department):
                super().__init__(name, age, salary, id)
                self.department = department

            def display(self):
                print(
                    f"Person name is {self.name} and age is {self.age} Salary is {self.salary} ID is {self.id} and Department is {self.department}"
                )

        m1 = Manager(name, age, salary, id, department)

        m1.display()

        print(issubclass(Manager, Employee))

    elif choice == 4:

        name = input("Employee Name: ")
        age = input("Employee Age: ")
        salary = int(input("Enter Salary: "))
        id = input("Enter ID: ")
        language = input("Enter language: ")

        class Developer(Employee):

            def __init__(self, name, age, salary, id, language):
                super().__init__(name, age, salary, id)
                self.language = language

            def display(self):
                print(
                    f"Person name is {self.name} and age is {self.age} Salary is {self.salary} ID is {self.id} and language is {self.language}"
                )

        d1 = Developer(name, age, salary, id, language)
        d1.display()

        print(issubclass(Developer, Employee))

    elif choice == 5:

        print("Choose details to show:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")

        show_details_choice = int(input("Enter Your Choice: "))

        if show_details_choice == 1:
            p1.display()

        elif show_details_choice == 2:
            print(Emp1.get_id_salary())

        elif show_details_choice == 3:
            m1.display()

        elif show_details_choice == 4:
            d1.display()

    elif choice == 6:

        print("\nChoose two employees to compare salaries.")

        id1 = input("Enter First Employee ID: ")
        id2 = input("Enter Second Employee ID: ")

        emp1 = None
        emp2 = None

        if Emp1 is not None:

            if Emp1.id == id1:
                emp1 = Emp1

            if Emp1.id == id2:
                emp2 = Emp1

        if m1 is not None:

            if m1.id == id1:
                emp1 = m1

            if m1.id == id2:
                emp2 = m1

        if d1 is not None:

            if d1.id == id1:
                emp1 = d1

            if d1.id == id2:
                emp2 = d1

        if emp1 is None or emp2 is None:

            print("Employee ID not found!")

        elif emp1 is emp2:

            print("Enter two different Employee IDs!")

        elif emp1 < emp2:

            print(emp1.name, "has a lower salary than", emp2.name)

        elif emp1 > emp2:

            print(emp1.name, "has a higher salary than", emp2.name)

        else:

            print("Both employees have equal salaries!")

    elif choice == 6:

        print("Thanks")
        break

    else:

        print("Invalid Choice!")
