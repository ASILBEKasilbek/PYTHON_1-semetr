def sumaandb(a,b):
    s=0
    for i in range(a+1,b):
        s+=i
    return s
a=int(input())
b=int(input())
print(sumaandb(a,b))