import random

attemps = []
x = random.randint(1, 20)
number = int(input("Try to guess the number: "))
    
def logic():
    if number > x:
        print("It's lower")
        attemps.append(number)
    elif number < x:
        print("It's higher")
        attemps.append(number)

def win():
    print(f"You win the number is: {x}")
    print(f"You nailed it in {str(len(attemps))} attemps")
    print("=== Your attemps ===")
    show_attemps()

def show_attemps():
    for n in attemps:
        print(f"** {n} **")

while number != x:
    print(x) 
    logic()
    number = int(input("Try again: "))

win()