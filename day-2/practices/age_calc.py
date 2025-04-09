print("** Life Time Calculator **")

user_age = input("¿Cuál es tu edad actual? ")
user_age = int(user_age)

target_age = int(input("¿Hasta qué edad quieres calcular? "))

remaining_years = target_age - user_age
days_remaining = remaining_years * 365
weeks_remaining = remaining_years * 52
months_remaining = remaining_years * 12

print(f"Te quedan {days_remaining} días, {weeks_remaining} semanas y {months_remaining} meses de vida (si llegas a los {target_age} años).")