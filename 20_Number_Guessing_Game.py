
import random

print("Welcome to the Number Guessing Game! ")
print("I'm thinking of a number between 1 and 100.")
diffculty=input("Choose a difficulty. Type 'easy' or 'hard': ")

if diffculty=='easy':
    attempts=10
else:
    attempts=5

number_choosen=random.randint(1,100)
while True:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess_number=int(input("Make a guess: "))

    if guess_number>number_choosen:
        print("Too high.")
        attempts-=1
    elif guess_number<number_choosen:
        print("Too low.")
        attempts-=1
    else:
        print(f"You got it! The answer was {number_choosen}")
        break

    if attempts==0:
        print("You've run out of guesses, you lose.")
        break

    print("Guess again")





