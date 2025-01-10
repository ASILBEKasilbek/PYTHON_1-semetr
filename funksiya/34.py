def factorial(n):
    s=1
    for i in range(n):
        s*=(i+1)
    return s
n=int(input())
print(factorial(n))