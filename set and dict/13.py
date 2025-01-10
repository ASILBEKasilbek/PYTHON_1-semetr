a=dict(item.split(':') for item in input().split())
k=list(a.keys())
for i in k:
    a.pop(i)
print(a)