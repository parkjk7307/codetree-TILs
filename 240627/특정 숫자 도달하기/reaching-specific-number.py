x = list(map(int,input().split()))

n = len(x)
sum_val = 0
count = 0

for i in range(n):
    if x[i] >= 250:
        break
    else:
        sum_val += x[i]
        count +=1

print(sum_val,f"{sum_val/count:.1f}", end = " ")