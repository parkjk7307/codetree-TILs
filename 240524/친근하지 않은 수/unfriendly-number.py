x = int(input())
count1 = 0
count2 = 0

for i in range(1,x+1):
    if (i % 2 == 0 or i % 3 == 0 or i % 5 == 0):
        count1 += 1
        continue
    count2 += 1 
print(count2)