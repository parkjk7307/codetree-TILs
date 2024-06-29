x = int(input())


cnt = 0

for i in range(x):
    y = list(map(int,input().split()))
    sum_val = 0 
    for j in y:
        sum_val += j
    
    c = sum_val/4
    if c >= 60:
        print("pass")
        cnt += 1
    elif c < 60:
        print("fail")

print(cnt)