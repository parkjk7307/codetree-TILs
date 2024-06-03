n = input().split()

a = int(n[0])
b = int(n[1])

c = (b-a)//2+1
d = b

for i in range(9):
    for j in range(c):
        print(f"{b} * {i+1} = {b * (i+1)}", end = "")
        b -= 2
        if j < c-1:
            print(" / ", end = "")
    b = d
    print()