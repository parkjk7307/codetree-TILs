x = int(input())


p = False
cnt = 0

for i in range(2 , x):
    if x % i == 0:
        p = True

if p == True:
    print("C")
else:
    print("N")