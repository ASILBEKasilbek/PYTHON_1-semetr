def  sort3(a,b,c):
    s=a+b+c
    if a>b>c or a>c>b:
        max1=a
    elif b>c>a or c>a>b:
        max1=a
    else:
        max1=b
    if a<b<c or a<c<b:
        min1=a
    elif b<c<a or c<a<b:
        min1=a
    else:
        min1=b
    return max1,s-max1-min1,min1
a=int(input())
b=int(input())
c=int(input())
print(sort3(a,b,c))