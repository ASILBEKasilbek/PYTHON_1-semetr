def tub(n):

    if n <= 1:
        return False
    else:
        a = True
        for i in range(2, int(n ** 0.5) + 1):  
            if n % i == 0:
                a = False
                break
        return a
n = int(input("Sonni kiriting: "))
print(tub(n))