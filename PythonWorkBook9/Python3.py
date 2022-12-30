from replit import clear
from Python4 import logo 

bids = {}
bidding_finished = False 

def find_highest_bidder(bidding_record):   
    higest_bid = 0
    winner = ""
    for bidder in bidding_record: 
        bid_amount = bidding_record[bidder]
        if bid_amount > higest_bid:
            higest_bid = bid_amount
            winner = bidder 
    print("The winner is {winner} with a bid of $ {higest_bid}")

print(logo)
print("Welcome to the secret auction program")

while not bidding_finished:
    name = input("What is your name?: ")
    price = input("What is your bid?: $")
    bids[name] = price 
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.") 
    if should_continue == "no":
        bidding_finished = True 
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()