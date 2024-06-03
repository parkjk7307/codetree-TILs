n = int(input())
a = 0
for i in range(n):
    for j in range(i+1):
        print(n-i+a, end = " ")
        a += 1
    a = 0
    print()