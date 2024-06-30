x = list(map(int,input().split()))
k = 0

for i in range(10):
    if x[i] % 3 == 0:
        k = i
        break
    
print(x[k-1])