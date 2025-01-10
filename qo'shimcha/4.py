def asilbek(k, n, t):
    d = int(k, n)
    if t == 10:
        return str(d)
    result = ''
    while d > 0:
        remainder = d % t
        result = str(remainder) + result
        d //= t
    
    return result or "0"

k =input() 
n =int(input()) 
t =int(input())
print(asilbek(k, n, t))
