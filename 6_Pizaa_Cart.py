print("Welcome to the PIZZA CART !")
pizza_size=input("What size pizza do you want? S, M or L: ")
pepperoni=input("Do you want pepperoni on your pizza? Y or N: ")
cheese=input("Do you want extra cheese? Y or N: ")
price=0
if pizza_size=='S':
    price=15
    if pepperoni =='Y':
        price+=2
    if cheese=='Y':
        price+=1
elif pizza_size=='M':
    price=20
    if pepperoni == 'Y':
        price+=3
    if cheese=='Y':
        price+=1
else:
    price=25
    if pepperoni == 'Y':
        price+=3
    if cheese=='Y':
        price+=1

print(f"Your final bill is ${price}")
