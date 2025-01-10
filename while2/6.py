


# a=list(map(int,input().split()))
# print(min(a))



n=int(input())
t=[]
for i in range(n):
    k=int(input())
    t.append(k)
max=t[0]
for i in t:
    if max>i:
        max=i
print(max)
