#x = list(map(str,input().split()))
#
#for i in range(9,-1,-1):
#    print(x[i], end = "")

x = list(map(str,input().split()))
reverse = x[::-1]

for i in reverse:
    print(i,end = "")