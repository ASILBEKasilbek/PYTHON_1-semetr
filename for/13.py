
n=int(input())
# print((n%2==0)*'-0.1',(n%2==1)*'0')
s=0
k=1
for i in range(11,11+n):
    s=s+k*i
    k=k*(-1)
print(s/10)
