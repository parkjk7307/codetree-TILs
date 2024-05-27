p = True

for i in range(5):
    x = int(input())
    if x % 3 != 0:
        p = False

if p == False:
    print("0")
else:
    print("1")