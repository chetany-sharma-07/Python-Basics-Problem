from data import MENU,resources

def generate_report():
    for i in resources:
        if i=="water" or i=="milk":
            print(f"{i.capitalize()}: {resources[i]}ml")
        if i=="coffee":
            print(f"{i.capitalize()}: {resources[i]}g")
    print(f"Money: ₹{money}")

def suffcient_drink(drink):
    insufficent_ingredient=[]
    global suffcient
    for ingredient in resources:
        if resources[ingredient]<MENU[drink]["ingredients"][ingredient]:
            insufficent_ingredient.append(ingredient)
            suffcient=False
    return insufficent_ingredient

def process_money(entered_money,drink):
    global money
    if entered_money>MENU[drink]["cost"]:
        change_money=entered_money-MENU[drink]["cost"]
        money+=MENU[drink]["cost"]
        print(f"Here is {change_money} in change.")
        return False
    elif entered_money<MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return True
    else:
        money+=entered_money
        return False

def transaction_successful(drink):
    for ingredient in resources:
        resources[ingredient]-=MENU[drink]["ingredients"][ingredient]
    print(f"Here is your {drink}. Enjoy!")
    return True

money=0
suffcient=True

while True:
    prompt=input("What would you like? (espresso/latte/cappuccino): ")

    if prompt=="report":
        generate_report()

    elif prompt=="off":
        break

    else:
        insuffient_ingredient=suffcient_drink(drink=prompt)
        if suffcient==False:
            message="Sorry there is not enough"
            for i in insuffient_ingredient:
                message+=", "+i
            print(message)
            continue
        
        ten=int(input("Enter number of notes(₹10): "))
        twenty=int(input("Enter number of notes(₹20): "))
        fifty=int(input("Enter number of notes(₹50): "))
        hundred=int(input("Enter number of notes(₹100): "))
        entered_money=10*ten+20*twenty+50*fifty+100*hundred
        not_enough_money=process_money(entered_money,drink=prompt)
        if not_enough_money:
            continue

        if transaction_successful(drink=prompt):
            continue
    

