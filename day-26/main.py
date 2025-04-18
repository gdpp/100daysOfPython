import random

numbers = [1, 2, 3]

new_list = [n + 1 for n in numbers]

print(new_list)

name = 'gustavo'

name_letters = [l for l in name]

print(name_letters)

range_list = [n * 2 for n in range(1, 5)]

print(range_list)

# comprehension list with if

names = ["Alex", "Dave", "Charlie", "Bob", "Ethane", "Fionas"]

short_names = [name for name in names if len(name) < 5]

print(short_names)

upper_names = [name.upper() for name in names if len(name) > 5]

print(upper_names)

# DICTIONARY COMPREHENSION
# new_dict = {NEW_KEY:NEW_VALUE for (key, value) in dict.items()}

names_v2 = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores = {student:random.randint(55, 100) for student in names_v2}

print(students_scores)

passed_students = { student:score for (student, score) in students_scores.items() if score > 70 }

print(passed_students)