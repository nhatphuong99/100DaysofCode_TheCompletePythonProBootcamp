from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def play():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    num = random.randint(1, 100)

    attempts = set_difficulty()
    guess = 0
    while guess != num:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        attempts = check_num(guess, num, attempts)
        if attempts > 0 and guess == num:
            return

        if attempts == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != num:
            print("Guess again.")

def check_num(guess, num, attempts):
    if guess > num:
        print("Too high!")
        return attempts - 1
    elif guess < num:
        print("Too low!")
        return attempts - 1
    else:
        print(f"You got it! The answer was {num}")
        return attempts - 1


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    while difficulty not in ["easy", "hard"]:
        difficulty = input("You must type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


play()