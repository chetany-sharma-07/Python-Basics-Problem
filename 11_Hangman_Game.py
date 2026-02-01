import random

word_list=["aardvark", "baboon", "camel"]

choosen_word=random.choice(word_list)
print(choosen_word)

placeholder=""
for position in range(len(choosen_word)):
    placeholder+="_"
print(placeholder)

display=""
guess_letter=input("\nGuess a letter: ").lower()
    
for letter in choosen_word:
    if guess_letter == letter:
        display+=letter
    else:
        display+="_"
print(display) 

while choosen_word != display:
    guess_letter=input("\nGuess a letter: ").lower()
    
    for position,letter in enumerate(choosen_word):
        if guess_letter == letter:
            tempList=list(display)
            tempList[position]=guess_letter
            display="".join(tempList)
    print(display)
    
if "_" not in display:
    print("You've Won")
