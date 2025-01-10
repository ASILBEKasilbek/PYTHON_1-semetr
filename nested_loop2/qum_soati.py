import os
import time 
n=int(input('->'))
t=[i for i in range(1,n,2)]
x=[0 for i in range(1,n,2)]
b=0
if n%2==0:
    t1=1
else:
    t1=0
while True:
    a=1
    print('*'*(n+2+t1),flush=True)
    t.reverse();x.reverse()
    p=0
    for i in t:
        print(' '*a+'*'+'*'*i+' '*x[p]+'*',flush=True)
        a+=1;p+=1
    t.reverse();x.reverse()
    print(' '*a+'*',flush=True)
    a-=1
    p=0
    for i in t:
        print(' '*a+'*'+' '*i+x[p]*'*'+'*',flush=True)
        a-=1
        p+=1
    if t[-1]==0:
        quit()
    if t[b]>0:
        t[b]=t[b]-1
        x[b]=x[b]+1
    if t[b]==0:
        b+=1
    print('*'*(n+2+t1),flush=True)
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')