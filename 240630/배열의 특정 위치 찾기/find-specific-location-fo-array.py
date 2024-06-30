x = list(map(int,input().split()))

n = len(x)
sum_val1 = 0
for i in range(2,n+1,2):
    sum_val1 += i

cnt = 0
sum_val2 = 0
for i in range(0,n,1): 
    if i % 3 == 0 and i != 0:
        sum_val2 += i
        cnt +=1
print(sum_val1,f"{sum_val2/cnt:.1f}")