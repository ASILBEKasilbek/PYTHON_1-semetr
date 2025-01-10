def issquare(n):
    x = 1
    while x * x < n:
        x += 1
    if x * x == n:
        return "kvadrat"
    else:
        return "kvadrat son emas."

n=float(input())
print(issquare(n))