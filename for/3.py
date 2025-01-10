a=int(input())
b=int(input())
t=[]
s=0
for i in range(a+1,b):
    t.append(i)
    s+=1
print(s)
print(*t)