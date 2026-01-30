import random
print("Welcome to ROCK PAPER SCISSOR GAME")
choice=["Rock","Paper","Scissor"]
your_choice=int(input("What do you want to choose?\nChoose 0 for Rock , 1 for Paper or 2 for Scissor.\n"))
computer_choice=random.randint(0,2)

print(f"Your choose: {choice[your_choice]}")
print(f"Computer choose: {choice[computer_choice]}")

if your_choice==computer_choice:
    print("It's Draw!")
elif your_choice == 0:
    if computer_choice == 1:
        print("You lose")
    else:
        print("You Win")
elif your_choice == 1:
    if computer_choice == 0:
        print("You Win")
    else:
        print("You lose")
else :
    if computer_choice == 0:
        print("You lose")
    else:
        print("You Win")
    
