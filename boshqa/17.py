a=float(input())
b=float(input())
c=float(input())
if (a<b and b<c ) or (a>b and b>c):
    print(a*2,b*2,c*2)
else:
    print(-a,-b,-c)