n=int(input())
for i in  range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print('1',end='')
        else:
            print('0',end='')
    print()