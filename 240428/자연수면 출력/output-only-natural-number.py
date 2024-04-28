x = input().split()

a = int(x[0])
b = int(x[1])

if a > 0 :
    for i in range(1, b+1):
        print(a, end = "")
else:
    print(0, end = "")