x = int(input())

for i in range(1,x+1):
    for j in range(1,i+1):
        
        print("*",end="")

    for p in range(1,i):
        print("*",end="")

    print()