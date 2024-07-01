arr = list(map(int,input().split()))

for i in range(10):
    arr.append((arr[-1]+arr[-2])%10)
    print(arr[i], end = " ")