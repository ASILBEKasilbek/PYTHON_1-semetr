n=int(input())
for i in  range(n):
    for j in range(n):
        if j==0 or i==0 or j==n-1 or i==n//2 or i==n-1 or j==n//2:
            print('#',end='')
        else:
            print('0',end='')
    print()