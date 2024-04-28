x = input().split()

a = int(x[0])
b = int(x[1])

if b > a :
    for i in range(b-a+1):
        print(b, end=" ")
        b-=1
elif a > b :
    for i in range(a-b+1):
        print(a, end=" ")
        a-=1
elif a == b :
    print(a)