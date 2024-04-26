x = input().split()

a = int(x[0])
b = int(x[1])

print(f"{a//b}.", end="")


a%=b
for i in range(20):
    a *= 10
    print(a //b, end ="")

    a%=b