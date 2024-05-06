# ROLLERCOASTER
print("Welcome to the rollercoaster")

height = int(input("What is your height in cm?: "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster.")
    
    age = int(input('What is your age?: '))

    # TICKETS
    if age < 12:
        print("Please pay $5")
        bill += 5;
    elif age <= 18:
        print('Please pay $7')
        bill += 7;
    elif age >= 45 or age <=55:
        print('Have a free ride on us')
    else:
        print('Please pay $12')
        bill += 12;

    wants_photo = input('Do you want a photo taken? Y or N. ')

    if wants_photo == 'Y':
        #add 3 dlls to bill
        bill += 3;

    print(f"your final bill is: ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
