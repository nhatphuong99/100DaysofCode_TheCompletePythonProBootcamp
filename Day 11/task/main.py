from art import logo
import random



def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

"""Calculate the user's and computer's scores based on their card values."""
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    """If an ace is drawn, count it as 11. 
    But if the total goes over 21, count the ace as 1 instead."""
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

"""Detect when computer or user has a blackjack. (Ace + 10 value card)."""
"""If computer gets blackjack, then the user loses 
(even if the user also has a blackjack). 
If the user gets a blackjack, then they win 
(unless the computer also has a blackjack)."""
"""Compare user and computer scores and see if it's a win, loss, or draw."""
def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    """Deal both user and computer a starting hand of 2 random card values."""
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        """Reveal computer's first card to the user."""
        print(f"Computer's first card: {computer_cards[0]}")


        """Game ends immediately when user score goes over 21 
        or if the user or computer gets a blackjack."""
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        else:  # Ask the user if they want to get another card
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    """Once the user is done and no longer wants to draw any more cards, 
    let the computer play. The computer should keep drawing cards
     unless their score goes over 16."""
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    """Print out the player's and computer's final hand
     and their scores at the end of the game."""
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))





while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    """After the game ends, ask the user if they'd like to play again. 
    Clear the console for a fresh start."""
    print("\n" * 20)
    play_game()

