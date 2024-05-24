a = int(input())
cnt = 0

while True:
    if a == 1:
        break
    elif a % 2 == 0:
        a = a // 2
        cnt += 1
    elif a % 2 == 1:
        a = a * 3 + 1
        cnt += 1
print(cnt)