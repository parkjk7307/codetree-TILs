a = input().split()

x = int(a[0])
y = int(a[1])

maxnum = x if x > y else y

print(maxnum)