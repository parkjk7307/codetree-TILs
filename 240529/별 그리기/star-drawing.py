n = int(input())

for i in range(n):
    for j in range((n-1)-i):
        print(" ",end="")
    for o in range((2*i)+1):
        print("*",end="")
    print()
for a in range(n-1):
    for b in range(a+1):
        print(" ",end = "")
    for c in range((2*n)-(2*a)-3):
        print("*", end="")
    print()