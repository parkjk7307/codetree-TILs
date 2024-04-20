a = input().split()
b = input().split()

x = int(a[0])
y = int(a[1])

o = int(b[0])
p = int(b[1])

if x > o and y > p:
    print(1)
else:
    print(0)