a=float(input())
n=int(input())
s=0
for i in range(1,n+1):
    print(a**i)
    s+=a**i
print(s)