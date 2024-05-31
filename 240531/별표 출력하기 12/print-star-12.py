n = int(input())

for i in range(n):
    if i == 0 :
        for _ in range(n):
            print("*", end = " ")
    else:
        for j in range(n):
            if j % 2 == 1 and i <= j :
                print("*", end = " ")
            elif i > j :
                print(" ", end = " ")
            else:
                print(" ",end = " ")
    print()    
#    else i % 2 != 0 :
#        for j in range()