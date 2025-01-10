def uzunlik(n):
    s=0;n=str(n)
    k=''
    while n!=k:
        k+=n[s]
        s+=1
    return s
k=input()
print(uzunlik(k))