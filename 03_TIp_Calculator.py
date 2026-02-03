#TIP CALCULATOR

print("Welcome to the tip calculator!")
total_bill=float(input("What was the total bill? $"))
tip_percentage=int(input("How much tip would you like to give? 10, 12, or 15? "))
no_of_people=int(input("How many people to split the bill? "))
bill_with_tip=total_bill+((tip_percentage/100)*total_bill)
each_person_to_pay=bill_with_tip/no_of_people
print("Each person should pay: $",round(each_person_to_pay,2))