a = int(input())

if a <= 7 :
    if a == 2 :
        print(28)
    elif a != 2 :
        if a % 2 == 1:
            print(31)
        elif a % 2 == 0:
            print(30)
elif a > 7:
    if a % 2 == 0:
        print(31)
    elif a % 2 == 1:
        print(30)