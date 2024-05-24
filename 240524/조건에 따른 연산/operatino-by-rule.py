x = int(input())
cnt = 0

while True:
    if x % 2 == 0 :
        x = x * 3 + 1
        cnt += 1
    elif x % 2 == 1 :
        x = x * 2 + 2
        cnt += 1
    if x >= 1000 :
        break
print(cnt)