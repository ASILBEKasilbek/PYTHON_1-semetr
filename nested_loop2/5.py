import time
n=int(input())
k=[];b=[]
for i in range(n-4,0,-2):
    k.append('*'*i)
for i in range(1,n-2,2):
    b.append(' '*i)
y=1;p=0;p1=0
b.reverse()
k.reverse()
while True:
    print('*'*n)
    t=1
    for i in b:
        print(t*' '+'*'+i+'*')
        t+=1
    print(t*' '+'*')
    t-=1
    for i in k:
        print(t*' '+'*'+i+'*')
        t-=1
    print('*'*n)
    time.sleep(1)
    print(b)
    try:
        qiymat= '*' + b[p][p1:]
        b[p]=qiymat
        y+=2;p+=1;p1+=1
    except:
        p1=0
        continue


        
    