a = input().split()

x = int(a[0])
y = int(a[1])
z = int(a[2])

if x <= y and x <= z:
    print(x)
elif y <= x and y <= z:
    print(y)
elif z <= x and z <= y:
    print(z)