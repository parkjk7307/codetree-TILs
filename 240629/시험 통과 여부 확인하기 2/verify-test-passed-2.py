x = int(input())
y = list(map(int,input().split()))

sum_val = 0  
cnt = 0

for i in range(x):
    for j in y:
        sum_val += j
    c = sum_val/4
    if c >= 60:
        print("pass")
        cnt += 1
        sum_val = 0
    elif c < 60:
        print("fail")

print(cnt)