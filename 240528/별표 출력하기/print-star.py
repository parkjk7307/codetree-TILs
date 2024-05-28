x = int(input())

for i in range(1,x+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

for a in range(1,x):
    for b in range(1,x - a+1):
        print("*",end=" ")
    print()