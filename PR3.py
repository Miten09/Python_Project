print("Welcome to the Student Data Organizer ")

my_all_students = []

while True:

    print("Select an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        student_id = int(input("Student ID: "))
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        date_of_birth = input("Date of Birth (YYYY-MM-DD): ")
        subjects = input("Subjects (comma-separated): ")

        my_subjects = set(subjects.split(","))

        id_dob = (student_id, date_of_birth)

        student_information = {
            "name": name,
            "id_dob": id_dob,
            "age": age,
            "grade": grade,
            "my_subjects": my_subjects,
        }

        my_all_students.append(student_information)

        print("Student added successfully ")

    elif choice == 2:

        if len(my_all_students) == 0:
            print("No student records found.")

        else:
            for student in my_all_students:

                print("----")
                print("Student ID:", student["id_dob"][0])
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Grade:", student["grade"])
                print("Date of Birth:", student["id_dob"][1])
                print("Subjects:", student["my_subjects"])

    elif choice == 3:

        search_id = int(input("Enter Student ID to update: "))

        for students in my_all_students:

            print(students)

            if students["id_dob"][0] == search_id:

                print("Choose option: ")
                print("1. Select Age: ")
                print("2. Select Subjects: ")

                option = int(input("Choose option: "))

                if option == 1:

                    new_age = int(input("Enter new age: "))
                    students["age"] = new_age

                elif option == 2:
                    new_subjects = input("Enter new subjects: ")
                    students["my_subjects"] = set(new_subjects.split(","))

                else:
                    print("Invalid Choice")

                break
            else:
                print("Student not found")

    elif choice == 4:

        search_id = int(input("Enter Student ID to delete: "))

        for students in my_all_students:

            if students["id_dob"][0] == search_id:

                my_all_students.remove(students)
                break
            else:
                print("Student not found")

    elif choice == 5:

        all_students_subjects = set()

        for students in my_all_students:

            all_students_subjects.update(students["my_subjects"])

        print("ALl Student Subject", all_students_subjects)
    elif 6:
        print("Thank the user")
        break
