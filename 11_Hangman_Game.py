import random

word_list=["aardvark", "baboon", "camel"]

choosen_word=random.choice(word_list)
print(choosen_word)

placeholder=""
for position in range(len(choosen_word)):
    placeholder+="_"
print(placeholder)

guess_letter=input("\nGuess a letter: ").lower()
 
display=""
for letter in choosen_word:
    if guess_letter == letter:
        display+=letter
    else:
        display+="_"
print(display)