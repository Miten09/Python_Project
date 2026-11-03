print("Welcome to the pattern generator and number analyzer!")

print("Select an option: ")
print("1. Generate a pattern")
print("2. Analyze a Range of Numbers")
print("3. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("1. Right Angled Triangle")
    print("2. Pyramid")
    print("3. Left-Angled Triangle")
    pattern_choice = int(input("Enter you choice: "))
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