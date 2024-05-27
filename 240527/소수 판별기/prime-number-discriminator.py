x = int(input())

p = True

for i in range(2, x):
    if i % x == 0:
        p = False
if p == False:
    print("C")
else:
    print("P")