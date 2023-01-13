import os
from art1 import logo
print(logo)
Auction_bids ={}

def highest_bidder(bidding_account):
    highest_bid = 0
    winner = ""
    for bidder in bidding_account:
        bid_amount = bidding_account[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"{winner} has the highest bid with ${highest_bid}")



shall_continue = True
while shall_continue:
    x = input("What is your name? \n")
    y = int(input("What amount do you want to bid? \n$"))
    Auction_bids[x] = y
    consent = input("is there anymore members ready for bid? Type yes to continue and no for the answer").lower()
    if consent == "no":
        shall_continue = False
        os.system('clear')
        highest_bidder(bidding_account= Auction_bids)
    elif consent == "yes":
        os.system('clear')
        
