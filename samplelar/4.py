n=int(input())
for i in range(n):
    t=[]
    for j in range(n):
        if j%2==1:
            t.append(n-i+n*j)
        else:
            t.append(i+1+j*n)
    print(" ".join(str(x).rjust(2," ") for x in t))
