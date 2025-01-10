n=int(input())
k=1
s=0
for i in  range(n):
    for j in range(n):
        if j==n-1 or j==0:
            s+=k
        print(k,end='')
        k+=1
    print()
print(s)