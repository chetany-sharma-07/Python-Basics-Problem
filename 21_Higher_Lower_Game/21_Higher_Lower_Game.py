import random

from data import data


#print welcome message
print(" WELCOME TO HIGHER AND LOWER GAME ")

account_A=random.choice(data) #choosing random account A

score=0 #intial score taken as 0

while True:

    account_B=random.choice(data) #choosing random account B

    #this loops ensure account A should not be equal to account B
    while account_A==account_B:
        account_B=random.choice(data)

    #printing followers of both chosen account for testing
    print(f"\nA: {account_A['follower_count']}, B: {account_B['follower_count']}")

    #showing name , description and country name of account A and B
    print(f"\nCompare A: {account_A["name"]}, a {account_A["description"]}, from {account_A["country"]}.")
    print("VS")
    print(f"Against B: {account_B["name"]}, a {account_B["description"]}, from {account_B["country"]}.")

    option_chosen=input("\nWho has more followers? Type 'A' or 'B': ").upper() #taking input as A and B

    #this gives chosen account in a separate variable
    if option_chosen=="A":
        chosen_account=account_A
    else:
        chosen_account=account_B

    #this gives the higher follower account in seperate variable 
    if account_A["follower_count"]>account_B["follower_count"]:
        higher_follower_acc=account_A
    else:
        higher_follower_acc=account_B

    #checking chosen account is higher follower account or not
    if chosen_account==higher_follower_acc:
        score+=1 #increasing score for right option
        account_A=higher_follower_acc
    else:
        print(f"\nSorry, that's wrong. Final score: {score}") #showing final message for wrong option
        break
