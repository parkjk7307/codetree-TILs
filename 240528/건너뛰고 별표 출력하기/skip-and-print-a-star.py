x = int(input())

for i in range(1,x+1):
    for j in range(1,i+1):
        print("*",end = "")
    print()
    print()

for a in range(1, x+1):
    for b in range(x-a):
        print("*",end = "")
    print()
    print()