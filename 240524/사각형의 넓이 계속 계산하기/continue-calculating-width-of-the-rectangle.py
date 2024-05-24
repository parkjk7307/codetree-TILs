wide = 0

while True:
    x = input().split()
    a = int(x[0])
    b = int(x[1])
    c = x[2]

    if c != "C":
        wide = a * b
        print(wide)
        continue
    if c == "C":
        wide = a * b
        print(wide)
        break