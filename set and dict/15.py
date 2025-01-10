a=dict(item.split(':') for item in input().split())
k=map(int,list(a.values()))
print(max(k))