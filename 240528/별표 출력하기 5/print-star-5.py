x = int(input())

for i in range(x):
    for j in range(x-i):
        for a in range(x-i):
            print("*",end ="")
        print(end = " ")
    print()