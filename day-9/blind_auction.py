def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f'The winner is: {winner} with the highest bid: {highest_bid}')

print("***Welcome to blind auction***")

participants = {}
rsp = "y"

while rsp == "y":
    username = input('Whats your name buddy: ')
    bid_price = int(input("What's your bid price: "))

    participants[username] = bid_price

    rsp = input("Another user wants to bid? y/n: ")


find_highest_bidder(participants)





