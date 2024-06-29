a = list(map(int,input().split()))
b = len(a)

for i in range(b):
    if a[i] == 0:
        a.pop()
print(a)
b = len(a)

for i in range(b-1, -1,-1):
    
    print(a[i], end =" ")