x = int(input())
cnt = 0

for i in range(x):
    y = list(map(int,input().split()))
    sum_val = 0 #초기화
    for j in y:
        sum_val += j
    if sum_val/4 >= 60:
        print("pass")
        cnt += 1
    elif sum_val/4 >= 60:
        print("fail")
    

print(cnt)