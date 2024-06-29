a = list(map(int,input().split()))

cnt = 0
sum_val = 0

for i in a:
    if i == 0:
        break
    else:
        if i % 2 == 0:
            cnt += 1
            sum_val += i

print(cnt,sum_val)