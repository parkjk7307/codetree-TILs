n = int(input())

cnt = 1
a = 1
cnt2 = 2


for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print(cnt,end = " ")
            if j == n-1:
                cnt += 2
            else:
                cnt += 1
        else:
            print(cnt,end = " ")
            if j == n-1:
                cnt += 1
            else:
                cnt += 2
            
        

    print()