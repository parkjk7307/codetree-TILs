x = input().split()

a = int(x[0])
b = int(x[1])
c = int(x[2])

arr = [a, b, c]

print(sum(arr))
print(sum(arr)//len(arr))
print(sum(arr) - (sum(arr)//len(arr)))