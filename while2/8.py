


a=int(input())
s=0
for i in range(1,a-2):
    if a%i==0:
        s+=i
print(s==a)