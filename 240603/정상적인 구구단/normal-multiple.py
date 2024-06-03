n = int(input())

result = 0
for i in range(n):
    for j in range(n):
        result = (i+1) * (j+1)
        print(i+1,"*",j+1,"=",result, end = "")
        if j < n-1:
            print(", ",end = "")
    print()