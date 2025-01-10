def fib(n):
    s=[1];k=1
    for i in range(n-1):
        s.append(k)
        k=s[i+1]+s[i]
    return s[-1]
n=int(input())
print(fib(n))