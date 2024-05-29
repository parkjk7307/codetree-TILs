x = int(input())

for i in range(x):
    if i % 2 !=0:
        for _ in range(i+1):
            print("*",end=" ")
        print()
    else:
        print("*")