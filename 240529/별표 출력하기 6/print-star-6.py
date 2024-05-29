x = int(input())

for i in range(x):
    for a in range(i):
        print(" ",end=" ")
    for j in range((2 * x) - (2 * i) - 1):
        print("*",end=" ")


for i in range(n):
	for _ in range(i):
		print(" ", end=" ")
	for _ in range((2 * n) - (2 * i) - 1):
		print("*", end=" ")
	print()

# 모양에 맞게 아랫쪽 별을 출력합니다.
for i in range(n-2, -1, -1):
	for _ in range(i):
		print(" ", end=" ")
	for _ in range((2 * n) - (2 * i) - 1):
		print("*", end=" ")
	print()