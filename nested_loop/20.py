n=int(input())
k=1
s=0
for i in  range(n):
    for j in range(n):
        if (i>=j and j+i!=n-1 ):
            s+=k
        print(k,end='')
        k+=1
    print()
print(s)