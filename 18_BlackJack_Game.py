import random
import os
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

#this change 11 to 1 if user score going over 21
def ace_is_drawn(user_cards):
    while (11 in user_cards) and user_score>21:
        user_cards[user_cards.index(11)]=1

#pick cards by passsing no of cards require
def pick_cards(no_of_cards):
    picked_cards=[]
    for i in range(no_of_cards):
        picked_cards.append(random.choice(cards))
        if sum(picked_cards)>21:
            ace_is_drawn(picked_cards)
    return picked_cards

#it show all cards of user and first card of computer
def show_cards(user_cards,comp_cards):
     global user_score
     print(f"\nYour cards are: {user_cards}, Your score is: {user_score}")
     print(f"Computer's first card is: {comp_cards[0]}\n")

#it checks for black jack 
def check_black_jack(user_cards,comp_cards):
    if (11 in comp_cards) and (10 in comp_cards):
        show_all_cards(user_cards,comp_cards)
        print("\nYou lose, Computer gets the BlackJack")
        return True
    elif (11 in user_cards) and (10 in user_cards):
        show_all_cards(user_cards,comp_cards)
        print("\nYou Win, You gets the BlackJack")
        return True

#it gives the final bound and final score of user and computer cards
def show_all_cards(user_cards,comp_cards):
    print(f"\nYour final bound is: {user_cards}, Your final score is: {sum(user_cards)}")
    print(f"Computer's final bound is: {comp_cards}, Computer's final score is: {sum(comp_cards)}\n")



# here game starts

game_continue=input("\nDo you want to play BlackJack Game. If yes type 'y' or if no type 'n' ").lower()
os.system('cls')
while game_continue=='y':
    print("\n##########======>>>> WELCOME TO BLACK JACK GAME <<<<======#########")
    #2 random cards pick by user and computer
    user_cards=pick_cards(2)
    comp_cards=pick_cards(2)

    #calculating score for user and computer
    user_score=sum(user_cards)
    comp_score=sum(comp_cards)

    #showing all user cards and 1 computer card
    show_cards(user_cards,comp_cards)

    #If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
    
    #here checks for black jack cards 
    if check_black_jack(user_cards,comp_cards):
        game_continue=input("\nYou'd like to play again. Type 'y' for yes or 'n' for no: ")
        os.system('cls')
        continue

    #here checks user score is grater than 21.
    if user_score>21: 
        show_all_cards(user_cards,comp_cards)
        print("\nYou lose, You score goes over 21.")
        game_continue=input("\nYou'd like to play again. Type 'y' for yes or 'n' for no: ")
        os.system('cls')
        continue
    
    #here user can choose more cards
    while True:
        another_card=input("\nYou want to get another card. Type 'y' for yes or 'n' for no: ").lower()
        sum_is_greater=False
        if another_card=='y':
            user_cards=user_cards+pick_cards(1)
            user_score=sum(user_cards)
            show_cards(user_cards,comp_cards)
            if user_score>21: 
                sum_is_greater=True
                show_all_cards(user_cards,comp_cards)
                print("\nYou lose, You score goes above 21.")
                game_continue=input("\nYou'd like to play again. Type 'y' for yes or 'n' for no: ")
                os.system('cls')
                break
        else:
            break
    if sum_is_greater:
        continue
   
    #here computer cand pick card if comp_score is less than 17
    while comp_score<17:
        comp_cards=comp_cards+pick_cards(1)
        comp_score=sum(comp_cards)
        
    show_all_cards(user_cards,comp_cards)
    
    #here all remaining conditions checks of win or lose
    if comp_score>21:
        print("\nYou Win, Computer score goes above 21.")
    elif comp_score>user_score:
        print("\nYou lose, you score less than Computer")
    elif user_score>comp_score:
        print("\nYou Win, you scored more than Computer")
    else:
        print("It's Draw, Both score same.")

    os.system('cls')
    game_continue=input("\nYou'd like to play again. Type 'y' for yes or 'n' for no: ")