n = int(input())
i = 1

while n >= i :
    if i % 3 == 0 :  
        print(0, end = " ")
    elif 20 > i and i > 10 and i % 3 == 1:
        print(0, end = " ")
    elif 30 > i and i > 20 and i % 3 == 2:
        print(0, end = " ")
    elif 50 > i and i > 40 and i % 3 == 1:
        print(0, end = " ")
    elif 60 > i and i > 50 and i % 3 == 2:
        print(0, end = " ")
    elif 80 > i and i > 70 and i % 3 == 1:
        print(0, end = " ")
    elif 90 > i and i > 80 and i % 3 == 2:
        print(0, end = " ")
    elif i >= 30 and i < 40:
        print(0, end = " ")
    elif i >= 60 and i < 70:
        print(0, end = " ")
    elif i >= 90 and i < 100:
        print(0, end = " ")
    else :
        print(i, end = " ")

    i += 1