import random

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
from hangman_words import word_list

#TODO-2: - Import the stages from hangman_art.py and make this error go away.

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

#TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

    # Choose a Word: Start by selecting a word from a predefined list or by generating one randomly. This will be the word that the player has to guess.

    # Display Initial State: Display an initial state of the word to the player. Typically, this involves showing the word with blank spaces for each letter that needs to be guessed.

    # Take User Input: Ask the player to guess a letter. Make sure to validate the input to ensure it is a single letter and hasn't been guessed before.

    # Update Guessed Letters: Keep track of the letters the player has guessed so far.

    # Check Guess: Determine if the guessed letter is in the word. If it is, update the display to reveal the position(s) of the letter in the word. If not, decrement the number of attempts left.

    # Repeat Until End Condition: Continue the game until one of the end conditions is met, such as the player guessing the word correctly or running out of attempts.

    # End Game: When the game ends, display a message to the player indicating whether they won or lost, and reveal the correct word if they lost.

#     Choose a Word:
#         You can create a list of words for the game. These words can be related to a specific theme or randomly chosen from a larger set.
#         Alternatively, you can prompt the player to enter a word, though this might not be ideal for a traditional Hangman game.

#     Display Initial State:
#         Display the word to the player with underscores (_) representing each letter that needs to be guessed.
#         For example, if the word is "python", initially display it as "_ _ _ _ _ _".

#     Take User Input:
#         Prompt the player to guess a letter.
#         Validate the input to ensure it is a single letter and that the player hasn't already guessed it.

#     Update Guessed Letters:
#         Keep track of the letters the player has guessed so far. This can be stored in a list or another data structure.

#     Check Guess:
#         Determine if the guessed letter is in the word.
#         If the letter is in the word, update the display to reveal its position(s).
#         If the letter is not in the word, decrement the number of attempts left. Optionally, you can display a hangman figure as attempts decrease.

#     Repeat Until End Condition:
#         Continue the game until one of the end conditions is met:
#             The player correctly guesses the word.
#             The player runs out of attempts (i.e., the hangman is complete).

#     End Game:
#         When the game ends, display a message to the player indicating whether they won or lost.
#         If the player lost, reveal the correct word to them.
    