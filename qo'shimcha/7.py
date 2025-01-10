n=list(map(int,input().split()))
t=[]
a=len(n)
if a%2==1:
    k1=n[a//2]
while n!=[]:
    try:
        k=n[0]+n[-1]
        t.append(k)
        n.pop(0)
        n.pop(-1)
    except:
        continue
try:
    t[-1]=t[-1]-k1
    print(*t)
except:
    print(*t)