n=int(input())
k=int(input())
for i in range(1,n+1):
    for j in range(1,k+1):
        if j==k:
            print('5',end='')
        elif j==1:
            print('1',end='')
        else:
            print('*',end='')
    print()