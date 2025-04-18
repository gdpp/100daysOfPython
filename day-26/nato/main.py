import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {value.letter:value.code for (key, value) in data.iterrows()}
word = input("Enter a word: ").upper()
result = [ nato_dict[letter] for letter in word]

print(result)