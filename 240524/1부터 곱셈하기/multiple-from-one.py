a = int(input())
prod = 1
for i in range(1,11):
    prod *= i
    if prod >= a:
        break
print(i)