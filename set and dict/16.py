a=dict(item.split(':') for item in input().split())
print(dict(sorted(a.items(), key=lambda item: item[1])))