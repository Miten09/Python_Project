print('Welcome to the Interactive Personal Data Collector')

name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
height = float(input("Enter Your Height in meters: "))
favourite_number = int(input("Enter Your Favourite number: "))

print("Name: ",name,type(name),id(name))
print("Age: ",age,type(age),id(age))
print("Height:",height,type(height),id(height))
print("Favourite Number:", favourite_number,type(favourite_number),id(favourite_number))

print("Your birth year is approximately : ",2026-age ,"(based on your age)",age)

print("Thank you!")