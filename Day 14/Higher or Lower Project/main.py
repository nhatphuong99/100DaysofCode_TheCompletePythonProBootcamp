"""
- display art
- take 2 random people in game data
- ask player for a guess
- compare followers of those 2
- check if the player guess is correct
- get followers from each account
-- use if statement to check if player guess is correct
- give user feedback on their guess
- score keeping
- make the game repeatable
- making account at position b become the next account at position a
- clear the screen after each guess
"""
from art import logo, vs
from game_data import data
import random

# format the account data into printable format
def format_data(account):
    """Take the account data and returns the printable format"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc} from {account_country}."


# check if player is correct

def check_answer(guess, a_followers, b_followers):
    """Take the guess and check if the player guess is correct"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
# generate a random account from game data
    account_a = account_b
    account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

# ask player for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

# clear the screen
    print("\n"*20)
    print(logo)

# - get followers of each account
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

# - check if player's guess is correct
    is_correct = check_answer(guess, a_followers, b_followers)

# give the feedback
    if is_correct:
        score += 1
        print(f"You're right!. Current scores {score}")
    else:
        print(f"Sorry, that's wrong!. Final score {score}")
        game_should_continue = False

# making account at position b become the next account at position a