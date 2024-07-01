arr = list(map(int,input().split()))
z = len(arr)

for i in range(z):
    if arr[i] == 0:
        break
    else:
        if arr[i] % 2 == 1:
            print(arr[i]+3, end = " ")
        else :
            print(arr[i]//2, end = " ")