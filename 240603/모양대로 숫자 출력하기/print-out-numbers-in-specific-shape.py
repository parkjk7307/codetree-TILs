n = int(input())

cnt = 0

for i in range(n):
    for p in range(i):
        print(" ",end = " ")
    for j in range(n-i):
        print(f"{n-i-cnt}",end = " ")
        cnt += 1
    cnt = 0
    print()