a=dict(item.split(':') for item in input().split())
b=dict(item.split(':') for item in input().split())
a.update(b)
print(a)