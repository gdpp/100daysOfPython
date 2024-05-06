import random

random_number = random.randint(1, 10)

print(random_number)

random_float = random.random() * 5

print(round(random_float, 2))


# Lists

countries = ['Mexico', 'Canada', 'Sweden', 'Spain']


print(countries[0])
print(countries[-1])
print(countries[2])

countries[1] = 'USA'

print(countries)

countries.append("Brazil")

print(countries)


# dirty_dozen = ['Strawberries', 'Spinach', 'Kale', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears', 'Tomatoes', 'Celery', 'Potatoes']
fruits = ['Banana', 'Orange', 'Mango', 'Blueberries', 'Kiwi', 'Pineapple', 'Watermelon']
vegetables = ['Carrots', 'Broccoli', 'Asparagus', 'Bell Peppers', 'Cucumbers']

mix_of_food = [fruits, vegetables]