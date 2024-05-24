x = input().split()

a = int(x[0])
b = int(x[1])

prod = 1

for i in range(a,b+1):
    prod *= i

print(prod)