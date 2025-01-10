a1=int(input())
a2=int(input())
a3=int(input())
a4=int(input())
if (a1+a2+a3)%3==0:
    print(4)
elif (a1+a2+a4)%3==0:
    print(3)
elif (a1+a3+a4)%3==0:
    print(2)
else:
    print(1)