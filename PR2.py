print("Welcome to the pattern generator and number analyzer!")

print("Select an option: ")
print("1. Generate a pattern")
print("2. Analyze a Range of Numbers")
print("3. Exit")

choice = int(input("Enter your choice: "))

while choice < 1 or choice > 3:
    print("Invalid choice! Please enter 1, 2 or 3.")
    choice = int(input("Enter your choice: "))

if choice == 1:
    print("1. Right Angled Triangle")
    print("2. Pyramid")
    print("3. Left-Angled Triangle")

    pattern_choice = int(input("Enter you choice: "))

    while pattern_choice < 1 or pattern_choice > 3:
        print("Invalid pattern choice! Please enter 1, 2 or 3.")
        pattern_choice = int(input("Enter you choice: "))

    no_of_rows = int(input("Enter no of rows for pattern: "))

    while no_of_rows <= 0:
        print("Number of rows must be positive.")
        no_of_rows = int(input("Enter no of rows for pattern: "))

    if pattern_choice == 1:

        for i in range(1, no_of_rows + 1):
            for j in range(i):
                print("*", end=" ")
            print()

    if pattern_choice == 2:
        for i in range(1, no_of_rows + 1):

            for j in range(no_of_rows - i):
                print(" ", end=" ")

            for k in range(2 * i - 1):
                print("*", end=" ")

            print()

    if pattern_choice == 3:
        for i in range(1, no_of_rows + 1):

            for j in range(no_of_rows - i):
                print(" ", end=" ")

            for k in range(i):
                print("*", end=" ")

            print()

elif choice == 2:

    start_range = int(input("Enter Start Range: "))
    end_range = int(input("Enter end Range: "))

    while end_range <= start_range:
        print("End range must be greater than start range.")
        end_range = int(input("Enter end Range: "))

    sum = 0

    for i in range(start_range, end_range + 1):
        sum = sum + i

        if i % 2 == 0:
            print("Number is even", i)
        else:
            print("Number is odd", i)

    print(f"Sum of all numbers from {start_range} to {end_range} is", sum)

elif choice == 3:
    print("Exiting the program.Goodbye!")
