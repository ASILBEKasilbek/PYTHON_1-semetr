def palindrom(n):
    k=[]
    while n!=0:
        g=n%10;n//=10
        k.append(g)
    if len(k)%2!=0:
        k.pop(len(k)//2)
    for i in range(1,len(k)+1):
        if k[i-1]!=k[-i]:
            return False
    return True
n=int(input())
print(palindrom(n))