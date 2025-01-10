a=list(input().split())
s=len(a[0])
k=a[0]
for i in a:
    if s<len(i):
        k=i
        s=len(i)
print(k)