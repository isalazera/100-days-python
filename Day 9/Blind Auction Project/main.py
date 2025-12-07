import art
print(art.logo)

# TODO-4: Compare bids in dictionary
def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

more_bids = True
bids = {}
while more_bids :
    # TODO-1: Ask the user for input
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    more_players = input("Are there any more bidders? Type yes or no.").lower()
    # TODO-2: Save data into dictionary {name: price}
    bids[name] = bid
    # TODO-3: Whether if new bids need to be added
    if more_players == "yes":
        more_bids = True
        print("\n" * 20)
    else:
        more_bids = False
        find_highest_bidder(bids)



