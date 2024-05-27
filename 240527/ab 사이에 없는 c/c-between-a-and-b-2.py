x = input().split()

a = int(x[0])
b = int(x[1])
c = int(x[2])

p = True

for i in range(a,b+1):
    if i % c == 0:
        p = False

if p == False:
    print("NO")
else:
    print("YES")