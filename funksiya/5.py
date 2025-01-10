def tort(x1,y1,x2,y2):
    k=x2-x1 if (x1-x2<0) else x1-x2
    k1=y2-y1 if (y1-y2<0) else y1-y2
    return 2*(k+k1),k1*k    
x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
print(tort(x1,y1,x2,y2))