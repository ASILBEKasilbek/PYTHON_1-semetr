n=int(input())
for i in range(n):
    for j in range(n+10):
        if i==0 or j==0 or i==n//3-1 or i==n//3+1 or i==(n//3)*2-1 or i==(n//3)*2+1 or j==n+9 or i==n-1:
            print('*',end='')
        elif i==n//3 or i==(n//3)*2:
            print('#',end='')
        else:
            print(' ',end='')
    
    print()
for i in range(n//2):
    print('*')