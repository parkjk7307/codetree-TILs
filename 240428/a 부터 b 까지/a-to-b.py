x = input().split()

a = int(x[0])
b = int(x[1])

for i in range (a, b+1):
    if b >= i:
        if i % 2 == 1:
            print(i, end = " ")
            i *= 2
        elif i % 2 == 0:
            print(i, end = " ")
            i += 3