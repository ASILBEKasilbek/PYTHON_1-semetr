def kvadrat(a,b,c):
    n=b*b-2*a*c
    if n>0:
        return 2
    elif n<0:
        return 'bosh'
    else:
        return 1
a=int(input())
b=int(input())
c=int(input())
print(kvadrat(a,b,c))