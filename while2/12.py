a=list(map(int,input().split()))
juft=[i for i in a if i%2==1]
toq=[i for i in a if i%2==0]
print(*juft)
print(*toq)