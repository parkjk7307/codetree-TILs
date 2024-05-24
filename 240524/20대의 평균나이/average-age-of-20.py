sum_val = 0
cnt = 0
avg_val = 0
while True:
    x = int(input())
    if 19 < x < 30:
        sum_val += x
        cnt += 1
    else:
        break

print(f"{sum_val/cnt:.2f}")