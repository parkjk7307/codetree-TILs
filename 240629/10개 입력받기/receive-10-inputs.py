x = list(map(int,input().split()))
cnt = 0
sum_val = 0

for i in x:
    if i == 0:
        break
    else:
        sum_val += i
    cnt += 1

print(sum_val,f"{sum_val/cnt:.1f}")