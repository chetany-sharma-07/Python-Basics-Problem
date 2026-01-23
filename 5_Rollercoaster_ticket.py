print("Welcome to the Roller Coaster Ride")
heigth = int(input("Enter your height in cm: "))
bill=0
if heigth >= 120:
    print("You can ride the rollercoaster. ")
    age=int(input("Enter your age: "))
    if age<=12:
        bill=100
        print("Kids tickets are Rs. 100")
    elif age<=18:
        bill=150
        print("Youth tickets are Rs. 150")
    else:
        bill=200
        print("Adults tickets are pay Rs. 200")
    
    wants_photo=input("Do you want photo on the ride? Type y for YES and n for NO: ")
    if wants_photo=="y":
        #ADD 50 Rupee more
        bill+=50
    
    print(f"Your total bill is: Rs.{bill}")

else:
    print("Sorry your are not enough taller for ride. ")