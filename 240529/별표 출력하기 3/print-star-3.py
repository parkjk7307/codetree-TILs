x = int(input())

for i in range(x):
    for j in range(i):
        print(" ",end=" ")

    for o in range((2*x)-(2*i)-1):
        print("*",end=" ")
    print()