import time as t
a=23;b=59;c=59
while 1:
    if c==0:
        if b==0:
            if a==0:
                break
            a-=1
            b=59
        b-=1
        c=59
    c-=1
    print(a,':',b,':',c)
    t.sleep(1)