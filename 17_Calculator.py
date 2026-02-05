def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operation={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

def calculator():
    print("######### WELCOME TO MY CALCULATOR ############")
    n1=int(input("What's the first number?: "))
    for key in operation:
        print(key)
    continue_calculation=True
    while continue_calculation:
        op=input("Pick an operation: ")
        n2=int(input("What's the next number?: "))
        result=operation[op](n1,n2)
        print(f"{n1} {op} {n2} = {result}")
        decision=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation: ")
        if decision=='n':
            print("\n"*20)
            calculator()
        else:
            n1=result

calculator()

