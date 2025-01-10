from math import *
a=int(input())
b=int(input())
c=int(input())
if abs(b-a)<abs(c-a):
    print(abs(b-a))
else:
    print(abs(c-a))