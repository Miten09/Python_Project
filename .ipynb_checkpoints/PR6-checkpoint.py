print("Welcome to the numpy Analyzer!")

print("Choose an option: ")
print("1. Create a Numpy array")
print("2. Perform Mathematical Operations")
print("3. Combine or Split Arrays")
print("4. Search, Sort, or Filter arrays")
print("5. Compute Aggregates and Statistics")
print("6. Exit")

while True:

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        
        arrayChoice = int(input("Enter your choice: " ))
        
        if arrayChoice == 1:
            
            # no_of_rows = int(input("Enter number of rows: "))
            no_of_columns = int(input("Enter number of columns: "))
            elements = input("Enter 6 elements for the array seperated by space: ")
            
            class DataAnalytics:
                
                def __init__(self,array):
                    self.array = array
                    
                def display(self):
                    print("Array created successfully",self.array)
                    
                