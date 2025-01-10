a=list(map(int,input().split()))
d=sorted(a,reverse=True)
d1=sorted(a) 
if a==[]:
    print("yo'q")
    quit()
if (a==d and d[-1]!=d[-2]) or (a==d1 and (d1[-1]!=d1[-2])):
    print("Ha")
    quit()
if a[0]<a[1]:
    p=[]
    p.append(a[0])
    for i in range(1,len(a)):
        try:
            if p[i-1]<a[i]:
                p.append(a[i])
        except:
            continue
    t=[]
    for i in range(a.index(p[-1])+1,len(a)): 
        t.append(a[i])
    k=t.copy()
    k.sort(reverse=True)
    if p[-1]==k[0]:
        print("Yo'q")
        quit()
    if k==t:
        print("HA")
    else:
        print("yoq")
else:  
    p=[]
    p.append(a[0])
    for i in range(1,len(a)):
        try:
            if p[i-1]>a[i]:
                p.append(a[i])
        except:
            continue
    t=[]
    for i in range(a.index(p[-1])+1,len(a)): 
        t.append(a[i])
    k=t.copy()
    k.sort()
    if p[-1]==k[0]:
        print("Yo'q")
        quit()
    if k==t:
        print("HA")
    else:
        print("yoq")