a=int(input())
b=int(input())
if a==b:
    if a>b:
        b=a
    else:
        a=b
else:
    a=0
    b=0
print(a,b)