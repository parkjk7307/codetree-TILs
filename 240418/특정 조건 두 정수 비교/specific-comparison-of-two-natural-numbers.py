a = input().split()

x = int(a[0])
y = int(a[1])

q = "1" if x < y else "0"
w = "1" if x == y else "0" 

print(q,w)