n = int(input())

for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(i+1):
        print("@",end=" ")
    print()
for a in range(n-1):
    for b in range(n-a-1):
        print("@",end=" ")
    print()