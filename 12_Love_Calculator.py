def calculate_love_score(name1,name2):
    name1=name1.upper()
    name2=name2.upper()
    true=0
    love=0
    for i in name1:
        if i in 'TRUE':
            true+=1 
        if i in 'LOVE':
            love+=1 
    for j in name2:
        if j in 'TRUE':
            true+=1
        if j in 'LOVE':
            love+=1

    print(str(true)+str(love))


print("*******WELCOME TO LOVE CALCULATOR******")
name1=input("Enter First person name: ")
name2=input("Enter Second person name: ")

calculate_love_score(name1,name2)
