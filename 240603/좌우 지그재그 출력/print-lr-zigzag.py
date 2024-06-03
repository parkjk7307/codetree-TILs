n = int(input())

cnt = 1
b = 0

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print(cnt,end = " ")
        
        elif i % 2 != 0:
            print(f"{n*(i+1)-b}", end = " ")
            b += 1
            if j == n-1:
                b = 0
        cnt += 1
    print()