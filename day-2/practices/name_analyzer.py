print("Name scanner")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

current_year = 2025
new_year = current_year + age

print(f"Hello {name}, You are {age} years old. You'll be 100 in the year {new_year}. Only are {100 - age} years remaining.")