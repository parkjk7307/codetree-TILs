x = int(input())

p = True

for i in range(2, x):
    if x % i == 0:
        p = False
if p == False:
    print("C")
else:
    print("P")