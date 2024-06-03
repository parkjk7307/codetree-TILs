n = input().split()

a = int(n[0])
b = int(n[1])
c = (b-a)//2+2
d = 1
val = 2*d


for i in range(4):
    for j in range(b-a+1):
        print(f"{b-j} * {val * d} = {(b-j)*(val*d)} ", end = "")
        if j < b-a:
            print("/ ",end = "")
    d += 1
    print()