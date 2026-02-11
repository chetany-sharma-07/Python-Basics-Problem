import os

print("####################### WELCOME TO BLIND AUCTION PROGRAM ########################")

bidder={}
while True:
    bidder_name=input("What is your name?: ")
    bid=int(input("What's your bid?: $"))
    bidder[bidder_name]=bid
    any_other_bidder=input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    os.system('cls')
    if any_other_bidder=="no":
        break

print(bidder)

# winner_name=""
# winner_bid=0
# for bidder_name in bidder:
#     if bidder[bidder_name]>winner_bid:
#         winner_name=bidder_name
#         winner_bid=bidder[bidder_name]

winner_name=max(bidder,key=bidder.get)
winner_bid=bidder[winner_name]
print(f"The winner is {winner_name} with a bid of ${winner_bid}.")
