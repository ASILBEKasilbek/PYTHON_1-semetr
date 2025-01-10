n=int(input())
s=1
q=1,1
for i in range(n):
    s*=q
    q+=0.1
print(s)