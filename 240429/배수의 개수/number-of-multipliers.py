cnt = 0
cnt2 = 0

for i in range(10):
    a = int(input())
    if a % 3 == 0:
        cnt += 1
    if a % 5 == 0:
        cnt2 += 1

print(cnt, end = " ")
print(cnt2)