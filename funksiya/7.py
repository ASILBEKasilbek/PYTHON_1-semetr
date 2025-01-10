def invertdigit(n):
    s=''
    while n>0:
        s+=str(n%10)
        n//=10
    return int(s)
n=int(input())
print(invertdigit(n))