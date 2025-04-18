# 📝 List Comprehensions

square_list = [x ** 2 for x in range(10)]
print(square_list)

pairs = [x for x in range(50) if x % 2 == 0]
print(pairs)

upper_names = [name.upper() for name in ["Alex", "Dave", "Charlie", "Bob", "Ethane", "Fionas"]]
print(upper_names)

hat_trick = [x for x in range(1, 31) if x % 3 == 0]
print(hat_trick)

len_words = [len(word) for word in ['apple', 'banana', 'kiwi']]
print(len_words)

# 🧠 Dictionary Comprehensions

square_dict = {x:x ** 2 for x in range(1, 6)}
print(square_dict)

words_dict = {word:len(word) for word in ['apple', 'banana', 'kiwi'] if len(word) > 4}
print(words_dict)

random_strings = ["Rocket", "Climb", "Shot", "Wine", "Cellar"]
random_words_dict = {index:value for index, value in enumerate(random_strings)}
print(random_words_dict)

word = "programming"
vowels = "aeiou"
vowel_count = {v:word.count(v) for v in vowels if v in word}
print(vowel_count)

cities_celsius = {"New York": 10, "Los Angeles": 15, "Miami": 30}
cities_fahrenheit = {city: (temp * 9/5) + 32 for city, temp in cities_celsius.items()}
print(cities_fahrenheit)