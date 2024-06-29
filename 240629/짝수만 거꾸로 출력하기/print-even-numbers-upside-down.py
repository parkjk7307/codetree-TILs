x = int(input())
y = list(map(int,input().split()))

for i in range(x-1,-1,-1):
    if y[i] % 2 == 0:
        print(y[i], end = " ")