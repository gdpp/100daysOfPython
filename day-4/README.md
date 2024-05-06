# Day 4

## Objectives

In this day I learned about:

-   Randomization
-   Python lists

### List Methods

-   **append(x)** - Adds an item (x) to the end of the list.
-   **extend(iterable)** - Extends the list by appending all the items from the iterable.
-   **insert(i, x)** - Inserts an item at a given position. The first argument is the index of the element before which to insert.
-   **remove(x)** - Removes the first item from the list whose value is x. Raises a ValueError if there is no such item.
-   **pop([i])** - Removes the item at the given position in the list, and returns it. If no index is specified, pop() removes and returns the last item in the list.
-   **clear()** - Removes all items from the list.
-   **index(x[, start[, end]])** - Returns the index of the first item whose value is x. Optional arguments start and end are used to limit the search to a particular subsequence of the list.
-   **count(x)** - Returns the number of times x appears in the list.
-   **sort(key=None, reverse=False)** - Sorts the items of the list in place (the arguments can be used for sort customization).
-   **reverse()** - Reverses the elements of the list in place.
-   **copy()** - Returns a shallow copy of the list.

## Project of the day

**Rock, Paper, Scissors**

For this project, this is the way used to resolved:

#### Step 1: Set Up

-   I've imported **random** library to simulate computer choices

#### Step 2: User Input

-   Use input() function with the user to enter their choice: Rock, Paper, or Scissors.

#### Step 3: Computer Choice

-   Generate the computer's choice randomly. You can use random.choice() to select an item randomly from a list of options.

#### Step 4: Determine the Winner

-   Use conditional statements to compare the user's choice and the computer's choice based on the rules:

    Rock beats Scissors
    Scissors beats Paper
    Paper beats Rock

#### Step 5: Display the Result

-   Print results then display the winner.

2. Run the script:

```bash
    python game.py
```

[Go to Home](../README.md)
