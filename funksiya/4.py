a=float(input());b=float(input());c=float(input());p=(a+b+c)/2;s=(p*(p-a)*(p-b)*(p-c))**(1/2);print(s) if ((a+b>c and c+b>a and a+c>b) and (a>0 and b>0 and c>0)) else print('Xato')

