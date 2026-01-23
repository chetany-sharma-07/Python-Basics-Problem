height=float(input("Enter height: "))
weight=float(input("Enter weight"))
bmi=weight/(height**2)
print(int(bmi))

if (bmi < 18.5):
    print("underweight")
elif (18.5 <= bmi < 25):
    print("normal weight")
else:
    print("overweight")
    