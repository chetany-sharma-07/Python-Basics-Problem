import random

# different stages of hangman lifes
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list=["aardvark", "baboon", "camel"]

#   random word choosen from word_list
choosen_word=random.choice(word_list)
# print(choosen_word)

# generating blank _ equal to the length of choosen word
placeholder=""
for position in range(len(choosen_word)):
    placeholder+="_"
print(placeholder)


correct_letter=[] #use to store previously guessed correct letter of remembring later
game_over=False #decide game over or not
no_of_lifes=6 #total no of lifes

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

    if guess_letter not in choosen_word:
        print(stages[no_of_lifes])
        no_of_lifes-=1
        print(f"No of Lifes Remaining: {no_of_lifes+1}")
        if no_of_lifes==-1:
            game_over=True
            print("You lose")

    if "_" not in display:
        game_over=True
        print("You win. ")




