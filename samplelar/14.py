# a=int(input());b=int(input());k=lambda a,b: a+b;print(k(a,b));k=lambda a,b: a*b;print(k(a,b));k=lambda a,b: a/b;print(k(a,b));k=lambda a,b: a-b;print(k(a,b))

a=lambda x: x if 0<x<10 else "raqam emas"
n=input()
k=int(input())
for i in range(len(n)):
    if int(n[i])==k:
        print(True)
        quit()

print(False)
