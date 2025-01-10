def soliq(n):
    if 0<=n<=5000:
        return n
    elif 5000<n<=10000:
        return n-n*0.035
    elif 11000<n<=15000:
        return n-n*0.075
    elif 15000<n<=20000:
        return n-n*0.12
    else:
        return n-n*0.18
n=float(input())
print(soliq(n))