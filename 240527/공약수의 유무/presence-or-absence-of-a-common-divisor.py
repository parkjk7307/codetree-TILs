x = input().split()

a = int(x[0])
b = int(x[1])

p = False

for i in range(a, b+1):
    if (1920 % i == 0 and 2880 % i == 0):
        p = True

if p == True:
    print("1")
else:
    print("0")