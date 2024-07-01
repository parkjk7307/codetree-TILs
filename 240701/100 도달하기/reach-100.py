x = list(map(int,input().split()))



for i in range(1,100):
    if i <= 1:
        x.append(x[0])
        x[0] = 1
        print(x[0],x[i], end = " ")
    elif i > 1:
        x.append( x[-1]+ x[-2])
        print(x[i], end = " ")
        if x[i] > 100:
            break