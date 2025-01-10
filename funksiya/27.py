def issquare(n):
    x=1
    while 5**x<n:
        x+=1
    if 5**x==n:
        return True
    else:
        return False

n=float(input())
print(issquare(n))