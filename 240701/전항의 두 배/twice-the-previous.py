x = list(map(int,input().split()))

for i in range(10):
    x.append(x[-1]+x[-2]*2)
    print(x[i], end = " ")