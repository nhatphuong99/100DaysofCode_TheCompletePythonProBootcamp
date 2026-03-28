# TODO-1: Ask the user for input
from art import logo
print(logo)
auctions = {}


def find_highest_bid(auctions):
    max_bid = 0
    max_bidder = ""
    for key, value in auctions.items():
        if value > max_bid:
            max_bid = value
            max_bidder = key

    print(f"The winner is {max_bidder} with a bid of ${max_bid}")

# TODO-2: Save data into dictionary {name: price}


# TODO-3: Whether if new bids need to be added
continue_auction = True
while continue_auction:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))

    auctions[name] = bid

    over = input("Are there any other bider? Type 'yes' or 'no'.\n").lower()
    if over == "no":
        continue_auction = False
        find_highest_bid(auctions)
    else:
        print("\n" * 20)
# TODO-4: Compare bids in dictionary

