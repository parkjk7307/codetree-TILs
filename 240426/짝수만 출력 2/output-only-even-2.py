x = input().split()

a = int(x[0])
b = int(x[1])


while a >= b:
    if a % 2 == 0:
        print(a, end = " ")
    a -= 1