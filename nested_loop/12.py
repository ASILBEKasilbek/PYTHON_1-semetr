n=int(input())
for i in  range(n):
    for j in range(n):
        if i==j or i+j==n-1 or i==0 or j==0 or j==n-1 or i==n-1:
            print('0',end='')
        else:
            print('1',end='')
    print()