n = int(input())


cnt = 1

for i in range(n):
    for j in range(n):
        print(f"{2*cnt}", end = " ")
        cnt += 1
        if cnt > 4:
            cnt = 1
    print()