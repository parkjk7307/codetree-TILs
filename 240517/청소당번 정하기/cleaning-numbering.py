x = int(input())

a = 0
b = 0
c = 0

i = 1
for i in range(1,x+1):
    if i % 12 == 0:
        c += 1
    elif i % 3 == 0:
        b += 1
    elif i % 2 == 0:
        a += 1

print(a, end = " ")
print(b, end = " ")
print(c)