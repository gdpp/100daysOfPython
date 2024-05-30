# Day 11

## Objectives

In this day I applied all the learbed topics in the past week such as:

-   `print()` Function
-   Commenting
-   Debbuging
-   String Manipulation
-   Variables
-   Data types
-   f-String
-   Conditional statements
-   Logical operators
-   Code blocks
-   Scope
-   Python lists
-   `for` & `while` Loops
-   Functions
-   Range
-   Code blocks
-   Functions with parameters
-   Functions that return values

## Project of the day

**Blackjack**

###### Understand the Rules of the Game

-   The objective is to score 21 points or get as close as possible without going over.
-   Players compete against the dealer, not each other.
-   Cards 2 to 10 are worth their face value
-   Face cards (J, Q, K) are worth 10 points
-   The Ace can be worth 1 or 11 points.
-   Each player initially receives two cards, and can hit or stand.

###### Game Design

Defines the main components of the game:

-   Cards and Deck: Create a standard deck of 52 cards.
-   Players: Include at least one player and the dealer.
-   Game Mechanics: Manage the actions of hit, stand and determine the winner.

###### Initialize the Game

Implement the logic to initialize a new game:

-   Create and Shuffle the Deck: Create a list that represents a deck of cards and shuffle it randomly.
-   Dealing Cards: Deal two cards to each player and the dealer.

###### Implement Core Functions

Divide the game into specific functions:

-   Create Deck: A function to create and return a deck of cards.
-   Shuffle Deck: A function to shuffle the deck.
-   Deal Cards: A feature to deal cards to a player or the dealer.
-   Calculate Hand Value: A function to calculate the value of a player's or dealer's hand.
-   Show Cards: A feature to show a player's cards and the dealer's visible card.

###### Implement the Player Turn

Allow the player to make decisions:

-   Hit Cards: Add a card to the player's hand and check if he has exceeded 21 points.
-   Stand: End the player's turn.

###### Implement the Dealer's Turn

Define the rules for the dealer:

-   Dealer Rules: The dealer must hit cards until he reaches at least 17 points.
-   Show Dealer's Cards: Once the dealer finishes his turn, show all of his cards.

###### Determine the Winner

Develop logic to determine the outcome of the game:

-   Compare Hands: Compare the values ​​of the player's and dealer's hands.
-   Determine Result: Decide the winner based on who has the highest value without going over 21.

<!--
###### Add Additional Features

Enhance the game with optional features:


 Betting: Allow players to place bets at the start of the game.
 Multiple Players: Adapt functions to handle multiple players in a game.
 Card Division (Split): Allow the player to split the hand if the first two cards are the same.
 -->

###### Suggested Code Structure

Divide your code into sections to keep it organized:

-   Initialization Section: Create the deck and mix it.
-   Dealing Section: Deal cards to the players and the dealer.
-   Game Section: Implement player and dealer turn logic.
-   Result Section: Determine and show the winner.

## Project Structure:

<!--
```mermaid
    mindmap
    root((hangman.py))
        hangman_art.py
        hangman_words.py
``` -->

1. Run the script:

```bash
    python main.py
```

[Go to Home](../README.md)
