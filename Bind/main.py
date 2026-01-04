from art import logo
binders = {}

def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")

print(logo)
while True:
    name = input("Please enter your name: ")
    bid = int(input("Please enter your bid: "))
    cont = input("Are there any other bidders? Type 'yes or 'no'.\n")
    print("\n" * 20)
    binders[name] = bid
    if cont == 'yes':
        continue
    elif cont == 'no':
        find_highest_bidder(binders)
        break
    else:
        print("Only yes or no")
