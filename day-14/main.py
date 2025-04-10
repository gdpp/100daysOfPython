from game_data import data
import random

def print_formatted_data(pick: dict):
    """Take the pick data and returns the printable format. """
    name = pick["name"]
    desc = pick["description"]
    country = pick["country"]

    return f"{name}, a {desc}, from {country}."

def get_followers_count(pick: dict):
    return pick["follower_count"]

def check_answer(user_guess, followers_a, followers_b):
    """ Take a user's guess and the follower counts and returns if they git it right. """
    if followers_a > followers_b:
        return user_guess == "a"
    else:
        return user_guess == "b"
        
score = 0
game_should_continue = True
pick_b = random.choice(data)

while game_should_continue:
    # Greeting
    print("========== | HIGHER / LOWER | GAME ==========")

    # Generate random pick from game data
    pick_a = pick_b
    pick_b = random.choice(data)

    if pick_a == pick_b:
        pick_b = random.choice(data)

    # Format the pick data into printable format.

    print(f"Compare A: {print_formatted_data(pick_a)}")
    print("VS.")
    print(f"Compare B: {print_formatted_data(pick_b)}")

    # Ask user for a guess
    guess = input("Who has more followers?, Type 'A' or 'B': ").lower()

    # Clear the screen
    print("\n" * 10)

    # Check if user is correct.
    # Get followers count of each pick
    followers_a = get_followers_count(pick_a)
    followers_b = get_followers_count(pick_b)

    # Use a condition statement to check if user is correct
    is_correct = check_answer(guess, followers_a, followers_b)

    # Give user feedback on their guess
    # Score keeping
    if is_correct:
        score += 1
        print(f"You're right. Current score {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score {score}")

    # Making pick at position BB become the next pick at position A
