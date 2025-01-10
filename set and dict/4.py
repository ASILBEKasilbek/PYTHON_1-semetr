n=int(input())
s=set()
k=0
while k<n:
    a=set(map(int,input().split()))
    s=s.union(a)
    k+=1
print(s)