n=list(map(int,input().split()))
t=[]
for i in range(1,len(n)):
    t.append(n[i-1]+n[i])
print(t)