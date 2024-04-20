a = input().split()

x = int(a[0])
y = int(a[1])
z = int(a[2])

if x <= y and x <= z:
    print(1, end=" ")
else:
    print(0, end=" ")

if x == y and y == z:
    print(1)
else:
    print(0)