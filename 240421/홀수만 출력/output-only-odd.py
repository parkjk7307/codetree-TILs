a = input().split()

x = int(a[0])
y = int(a[1])

for i in range(x, y+1, 1):
    if i % 2 == 1:
        print(i, end = " ")