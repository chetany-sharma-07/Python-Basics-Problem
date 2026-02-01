import random

word_list=["aardvark", "baboon", "camel"]

choosen_word=random.choice(word_list)
print(choosen_word)

placeholder=""
for position in range(len(choosen_word)):
    placeholder+="_"
print(placeholder)

correct_letter=[]
game_over=False

while not game_over:
    display=""
    guess_letter=input("\nGuess a letter: ").lower()
        
    for letter in choosen_word:
        if guess_letter == letter:
            display+=letter
            correct_letter.append(guess_letter)
        elif letter in correct_letter:
            display+=letter
        else:
            display+="_"
    print(display) 

    if "_" not in display:
        game_over=True
        print("You win. ")




