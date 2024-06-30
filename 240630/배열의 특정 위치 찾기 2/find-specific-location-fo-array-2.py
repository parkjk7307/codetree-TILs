x = list(map(int,input().split()))

sum1 = 0
sum2 = 0
for i in range(10):
    if i % 2 == 0: #홀수번째
        sum1 += x[i]
for i in range(10):
    if i % 2 == 1: #짝수번째
        sum2 += x[i]

div = 0
if sum1 >= sum2:
   div =  sum1 - sum2
else:
    div = sum2 - sum1

print(div)