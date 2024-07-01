x = list(map(int,input().split()))

cnt = 0
for i in range(1,11):
    x.append(x[0]*i)
    print(x[i], end = " ")
    if x[i] % 5 == 0:
        cnt += 1
        if cnt == 2:
            break