print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
print("You're at the cross road. Where you want to go?")
left_right=input("\tType \"left\" or \"right\"\n")
if left_right=="right":
    print("Game Over!, You feel into a tunnel")
else:
    print("You've come to lake. There is an island in the midle of the lake. ")
    wait_swim=input("\tType 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if wait_swim=="swim":
        print("Game Over!, Attacked by Crocodile")
    else:
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        door_color=input("\tOne red, one yellow, one blue. Which colour do you choose?\n")
        if door_color=="red" or door_color=="blue":
            print("Game Over!")
        else:
            print("You Win!")

