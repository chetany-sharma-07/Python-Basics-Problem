import random
friends=["Alice","Bob","Charlie","David","Emanuel"]
random_num=random.randint(0,len(friends)-1)
match random_num:
    case 0:
        print(friends[0])
    case 1:
        print(friends[1])
    case 2:
        print(friends[2])
    case 3:
        print(friends[3])
    case 4:
        print(friends[4])

    