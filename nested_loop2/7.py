
n=int(input())
k=int(input())
t=0
x=n
for i in range(1,n+1):
    for j in range(1,k+1):
        if x==0:
            x+=2
            t-=1
        print(' '*t+'*'*x)
        t+=1;x-=2
    print()



    