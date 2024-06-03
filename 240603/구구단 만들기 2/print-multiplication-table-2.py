n = input().split()

a = int(n[0])
b = int(n[1])
c = (b-a)//2+2
d = 1
cnt = b
val = 2*d


for i in range(4):
    for j in range(c):
        print(f"{b-j} * {val * d} = {(b-j)*(val*d)} ", end = "")
        if j < c-1:
            print("/ ",end = "")
    d += 1
    print()