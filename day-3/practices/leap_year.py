print("= = [ L E A P    Y E A R    D E T E C T O R ] = =")

# 2024 Y
# 2100 N

year = int(input("Enter a year: "))

# Es divisible entre 4 
if year % 4 == 0:
    # Es divisible entre 100
    if year % 100 == 0:
        # Es divisible entre 400
        if year % 400 == 0:
            print(f"{year} is leap year")
        else:
            print(f"{year} is not leap year")
    else:
        print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")

# V.2.
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")
