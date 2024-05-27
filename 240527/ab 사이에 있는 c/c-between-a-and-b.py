x = input().split()

a = int(x[0])
b = int(x[1])
c = int(x[2])

setisfied = False

for i in range(a, b+1):
    if (i % c == 0):
        setisfied = True
        break

if setisfied == True:
    print("YES")
else:
    print("NO")