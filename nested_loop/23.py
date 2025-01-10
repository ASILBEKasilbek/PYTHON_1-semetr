n=int(input())
for i in  range(n):
    for j in range(n):
        if i>=j:
            print(j+1,end='')
    print()
