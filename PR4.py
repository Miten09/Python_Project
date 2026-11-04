print("Welcome to the data analyzer and transformer program")

print('Main Menu:')
print("1. Input Data")
print("2. Display Data summary (Built-in Functions)")
print("3. Calculate Factorial (Recursion)")
print("4. Filter Data by threshold (Lambda Function)")
print("5. Sort Data")
print("6. Display Dataset Statisctics (Return Multiple Values)")
print("7. Exit Program")


final_list = []

while True: 
    choice = int(input("Please Enter your choice: "))

    if choice == 1:
        array_1d = input("Enter data for 1D array (seperate by spaces): ")
        final_list = list(map(int, array_1d.split(" ")))
        print(final_list)
        
    elif choice == 2:
    
        if len(final_list) == 0:
            print("No values found")
            
        else:
            print("Total Elements: ",len(final_list))
            print("Minimum Value: ",min(final_list))
            print("Maximum Value: ",max(final_list))
            print("Sum of all values: ",sum(final_list))
            print("Average value: ",(sum(final_list) / len(final_list)))
    
    elif choice == 3:
        factorial_choice = int(input("Enter a number to calculate its factorial: "))
        
        def factorial(n):
            if n==1:
                return 1
            return n*factorial(n-1)
        print(factorial(factorial_choice))
        
    elif choice == 4:
        threshold_value = int(input("Enter a threshold value to filter out data below this value: "))
        
        filtered_value = list(filter(lambda x:x>threshold_value,final_list))
        print(filtered_value)
    
    elif choice == 5:
        print("Choosing sorting option:")
        print("1. Ascending")
        print("2. Descending")
        
        my_sort_choice = int(input("Enter your sort choice: "))
        
        if my_sort_choice == 1:
            final_list.sort()
            print(final_list)
        else:
            final_list.sort(reverse=True)
            print(final_list)
        
    elif choice == 6:
        
        def statistics(**kwargs):
            print("Dataset Statistics")
            for key,value in kwargs.items():
                print(f"- {key}:{value}")
        
        statistics(min_value=min(final_list),max_value=max(final_list),sum=sum(final_list),average=(sum(final_list)/len(final_list)))
    
    elif choice == 7:
        print("Thank you for using the Data Analyzer and transformer program.Goodbye!")