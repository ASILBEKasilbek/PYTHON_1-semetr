n=int(input())
for i in  range(n):
    for j in range(n):
        if i>=j:
            print(i+1,end='')
    print()
