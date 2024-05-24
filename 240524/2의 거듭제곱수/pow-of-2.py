x = int(input())
cnt = 0
while True:
    if x % 2 == 0:
        x //= 2
        cnt +=1
    if x == 1:
        break
print(cnt)