a = int(input())
count = 0

for i in range(1,a+1):
    if a > 1:
        a = a // i
        count += 1
        continue
    if a <= 1:
        break
print(count)