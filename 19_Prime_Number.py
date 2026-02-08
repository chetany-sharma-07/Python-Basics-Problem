def is_prime(num):
    if num==1:
        return False
    else:
        for i in range(2,int(num/2)+1):
            if num%i==0:
                return False
        return True


num=int(input("Enter a Number : "))
prime=is_prime(num)
if prime:
    print(f"{num} is a Prime Number")
else:
    print(f"{num} is not a Prime Number")