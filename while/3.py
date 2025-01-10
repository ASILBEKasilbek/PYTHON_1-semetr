n=int(input())
k=int(input())
p=0
while n>k:
    n=n-k
    p+=1
print(p,n)