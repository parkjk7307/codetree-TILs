x = int(input())

for i in range(x):
    for j in range(x-i):
        print("*",end=" ")
    print()

for i in range(x-1):
    for j in range(i+2):
        print("*",end=" ")
    print()