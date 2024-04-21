a = input().split()
b = input().split()

x = int(a[0])
y = int(a[1])

o = int(b[0])
p = int(b[1])

if x > o :
    print("A")
elif x == o and y > p:
    print("A")
elif x == o and y < p:
    print("B")
else:
    print("B")