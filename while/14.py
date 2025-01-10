n=int(input())
s=0
k=1
while s<n:
    s+=1/k
    k+=1
print(k-1,s-1/k)