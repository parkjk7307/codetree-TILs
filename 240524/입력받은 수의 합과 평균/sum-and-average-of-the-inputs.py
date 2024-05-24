x = int(input())

sum_val = 0
avg_count = 0
avg_val = 0

for i in range(1, x+1):
    y = int(input())
    sum_val += y
    avg_count += 1

avg_val = sum_val /  avg_count


print(sum_val, end = " ")
print(f"{avg_val:.1f}")