sum_val = 0
cnt = 0
avg_val = 0
while True:
    x = int(input())
    if (19 < x < 30):
        sum_val += x
        cnt += 1
        continue
    else:
        break

avg_val = sum_val / cnt

print(f"{avg_val:.2f}")