a = input().split()
b = input().split()

x = int(a[0])
y = a[1]

o = int(b[0])
p = b[1]

if ((x >= 19 or o >= 19) and (y == "M" or p == "M")):
    print("1")
else:
    print("0")