x = int(input())

check = 0

for i in range(1,x):
    if x % i == 0:
        check += i

if x == check:
    print("P")
elif x != check:
    print("N")