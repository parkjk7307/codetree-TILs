x = input().split()

a = int(x[0])
b = int(x[1])

while b >= a:
    if a % 2 == 1:
        print(a, end = " ")
        a *= 2
    elif a % 2 == 0:
        print(a, end = " ")
        a += 3