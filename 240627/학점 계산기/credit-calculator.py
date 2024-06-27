x = int(input())
y = list(map(float,input().split()))

z = sum(y)/x

print(f"{z:.1f}")

if z >= 4.0:
    print("Perfect")
elif z >= 3.0:
    print("Good")
else :
    print("Poor")