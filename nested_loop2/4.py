n=int(input())
k=n
t=0
for i in range(n//2):
    print(' '*t+'*'*k+' '*t)
    t+=1
    k-=2
for i in range(n//2):
    print(' '*t+'*'*k+' '*t)
    t-=1
    k+=2
print(n*'*')