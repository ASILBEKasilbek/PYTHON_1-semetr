def arif(a,b,op):
    if op==1:
        return a-b
    elif op==2:
        return a*b
    elif op==3:
        return a+b
    else:
        return a/b
    
a=int(input())
b=int(input())
op=int(input())
print(arif(a,b,op))