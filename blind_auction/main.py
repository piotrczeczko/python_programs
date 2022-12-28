from replit import clear
from art import *

bids = {}
bidding_finished = False

print(logo)


def find_highest_bidder(bidding_record):
    highest_bid = 0
    highest_bid_name = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            highest_bid_name = bidder
    print(f"The winner is {highest_bid_name} with a bod of ${highest_bid}.")



while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        clear()


# choose highest bid:




