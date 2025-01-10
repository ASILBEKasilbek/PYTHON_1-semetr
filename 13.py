# a=float(input());b=float(input());c=float(input());p=(a+b+c)/2;s=(p*(p-a)*(p-b)*(p-c))**(1/2);print(s) if ((a+b>c and c+b>a and a+c>b) and (a>0 and b>0 and c>0)) else print('Xato')

import os
import time as t

n='Loading'
k=1
while 1:
    if k%4==1:
        print(n+' ..')
    elif k%4==2:
        print(n+'. .')
    elif k%4==3:
        print(n+'.. ')
    else:
        print(n+'. .')
    k+=1
    t.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    

# os.system(f"yt-dlp -o - video13.mp4 | mplayer -vo caca -")
