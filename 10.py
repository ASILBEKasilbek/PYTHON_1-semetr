
n = int(input("Garage o'lchamini kiriting: "))
a = [[0] * n for i in range(n)]  
while True:
    r = input("Mashina nomini kiriting: ")
    col = int(input("Ustunni kiriting: "))-1
    row = int(input("Qatorni kiriting: "))-1
    if a[row][col]==0:
        a[row][col]=r
    else:
        t=[];
        k=[];
        s=[];
        p=0
        for i in range(n):
            for j in range(n):
                if a[i][j]==0:
                    t.append(i)
                    k.append(j)
                    s.append(abs(t[p]-col)+abs(k[p]-row));p+=1
        if 0 in s:
            s.remove(0)
        f=min(s)
        if f>5:
            continue
        
        while f==min(s):
            r=s.index(min(s))
            s.pop(r)
            print("Siz hozirda bu yerga mashina qo'ya olmaysiz mana bu koordinatalarga mashina qo'ysayiz buladi:")
            print(t[r]+1,k[r]+1)
        print(f"Bu yerda {a[row][col]} bor")
        continue
    for i in a:
        print(*i)