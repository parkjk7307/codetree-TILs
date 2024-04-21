a = input().split()

x = int(a[0])
y = int(a[1])

if x >= 90 :
    if y >= 95:
        print("100000")
    elif y >= 90:
        print("50000")
else :
    print("0")