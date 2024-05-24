sum_val = 0
avg_count = 0
avg_val = 0

for i in range(10):
    x = int(input())
    if (x >= 0 and x <= 200):
        sum_val += x 
        avg_count += 1
avg_val = sum_val / avg_count


print(sum_val, end = " ")
print(f"{avg_val:.1f}")