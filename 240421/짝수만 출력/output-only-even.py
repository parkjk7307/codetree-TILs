a = input().split()

x = int(a[0])
y = int(a[1])



while x <= y:
    if x % 2 == 0:
        print(x, end = " ")
    x += 1