import random

names = input("Enter names separated by comma: ")

names_list = names.split(',')

pos = random.randint(0, len(names_list))


print(f"The seat VIP is for {names_list[pos]}")
