a = input().split()
b = input().split()
c = input().split()

agam = a[0]
atem = int(a[1])

if (agam == "Y" and atem >= 37) :
    A = 'A'
elif (agam == "N" and atem >= 37) :
    A = 'B'
elif (agam == "Y" and atem < 37) :
    A = 'C'
else :
    A = 'D'


bgam = b[0]
btem = int(b[1])

if (bgam == "Y" and btem >= 37) :
    B = 'A'
elif (bgam == "N" and btem >= 37) :
    B = 'B'
elif (bgam == "Y" and btem < 37) :
    B = 'C'
else :
    B = 'D'

cgam = c[0]
ctem = int(c[1])

if (cgam == "Y" and ctem >= 37) :
    C = 'A'
elif (cgam == "N" and ctem >= 37) :
    C = 'B'
elif (cgam == "Y" and ctem < 37) :
    C = 'C'
else :
    C = 'D'


if (A == 'A' and B == 'A') or (A =='A' and C =='A') or (B =='A' and C =='A'):
    print("E")
else :
    print("N")