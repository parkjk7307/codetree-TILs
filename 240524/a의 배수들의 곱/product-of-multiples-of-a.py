x = input().split()

a = int(x[0])
b = int(x[1])

prod = 1

for i in range(1,b+1):
    if i % a ==0 :
        prod *= i

print(prod)