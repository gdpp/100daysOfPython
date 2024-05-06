import random

options = ['Rock', 'Paper', 'Scissors'] # [0, 1, 2]

usr_option = int(input("Choose 0 = Rock, 1 = Paper and 2 = Scissors"))
cpu_option = random.choice(options)

if usr_option >= 3 or usr_option < 0:
    print("Invalid option, game aborted!!!")

if usr_option == 0 and cpu_option == 2:
    print("User win!")
elif cpu_option == 0 and usr_option == 2:
    print("Cpu win!")
elif usr_option < cpu_option:
    print('Cpu win!')
elif usr_option > cpu_option:
    print('User win!')
elif usr_option == cpu_option:
    print('Draw!')

