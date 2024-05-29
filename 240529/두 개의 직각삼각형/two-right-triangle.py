x = int(input())

for i in range(x):
    for j in range(x-i):
        print("*", end = "")
    for o in range(i):
        print(" ",end = "")
    for b in range(i):
        print(" ",end = "")
    for a in range(x-i):
        print("*", end = "")
    print()