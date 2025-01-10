a=dict(item.split(':') for item in input().split())
if a:
    print("Bo'sh")
else:
    a.update({1:2})
    print(a)