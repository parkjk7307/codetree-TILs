x = input().split()

a = int(x[0])
b = int(x[1])

prod = 1

for i in range(b):
    prod *= a

print(prod)