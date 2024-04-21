a = input().split()

x = int(a[0])
y = int(a[1])
z = int(a[2])

if x > y and x > z :
    if y > z :
        print(y)
    elif y < z:
        print(z)

elif y > x and y > z :
    if x > z:
        print(x)
    elif x < z:
        print(z)

elif z > x and z > y :
    if x > y:
        print(x)
    elif x < y:
        print(y)