n=int(input("o'lchamni kiriting:"))

while n%2==0:
    n=int(input("iltimos o'lchamni toq son kiriting:"))
    while n%2==0:
        n=int(input("Ya hozirgina aytdim o'lchamni toq son kiriting deb:"))
        while n%2==0:
            n=int(input("Tushunmadizmi, o'lchamni toq son kiriting deb:"))
            while n%2==0:
                n=int(input("Ruschalab yoki Ingilizchalab aytaymi o'lchamni toq son kiriting deb:"))
                while n%2==0:
                    n=int(input("Agar o'lchamni toq son kiritmasayiz dasturni o'chiraman ohirgi imkoniz:"))
                    quit()



def harf_q(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or (j == n-1 and i < n-1) or (i == n//2 and j > n//2) or (i == j and i > n//2):
                print('*', end='')
            else:
                print(' ', end='')
        print()
def harf_e(n):
    for i in range(n):
        for j in range(n):
            if i==0 or j==0 or i==n-1  or i==n//2:
                print('*',end='')
            else:
                print(' ',end='')
        print('')
def harf_r(n):
    for i in range(n):
        for j in range(n):
            if (j==n-1 and i==n//2+1):
                print(' ',end='')
            elif i==0 or j==0 or (j==n-1 and i<n//2) or (i==n//2 and j<n-(n//2)//2) or (j==n-2 and j!=n-1 and i==n//2+1) or (j==n-1 and i>n//2):
                print('*',end='')
            else:
                print(' ',end='')
        print('')
def harf_t(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or j == n//2:
                print('*', end='')
            else:
                print(' ', end='')
        print()
def harf_y(n):
    for i in range(n):
        for j in range(n):
            if (i == j and i < n//2) or (i + j == n-1 and i < n//2) or (j == n//2 and i >= n//2):
                print('*', end='')
            else:
                print(' ', end='')
        print()
def harf_u(n):
    for i in range(n):
        for j in range(n):
            if j == 0 or j == n-1 or i == n-1:
                print('*', end='')
            else:
                print(' ', end='')
        print()
def harf_i(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == n//2:
                print('*', end='')
            else:
                print(' ', end='')
        print()
def harf_o(n):
    for i in range(n):
        for j in range(n):
            if (i==0 and j==0) or (i==0 and j==n-1) or (i==n-1 and j==0) or (i==n-1 and j==n-1):
                print(' ', end='')
            elif i == 0 or i == n-1 or j == 0 or j == n-1:
                print('*', end='')
            else:
                print(' ', end='')
        print()
def harf_p(n):
    for i in range(n):
        for j in range(n):
            if j == 0 or (i == 0 and j < n-1) or (i == n//2 and j < n-1) or (j == n-1 and i > 0 and i < n//2):
                print('*', end='')
            else:
                print(' ', end='')
        print()
def harf_a(n):
    for i in range(n):
        for j in range(n):
            if i==0 or j==n-1 or j==0 or i==n//2:
                print('*',end='')
            else:
                print(' ',end='')
        print('')
def harf_s(n):
    for i in range(n):
        for j in range(n):
            if (i==n-1 and j==0) or (i==0 and j==0) or (i==n//2 and j==n-1) or (i==n-1 and j==n-1) or (i==n//2 and j==0) or (i==0 and j==n-1):
                print(' ', end='')
            elif (i==n-2 and j==0) or (i==1 and j==n-1) or i == 0  or i == n-1 or i == n//2 or (j == 0 and i < n//2) or (j == n-1 and i > n//2):
                print('*', end='')
            else:
                print(' ', end='')
        print()
def harf_d(n):
    for i in range(n):
        for j in range(n):
            if (j==n-1 and i==0 or (i==n-1 and j==n-1)):
                print(' ',end='')
            elif i==0 or j==0 or i==n-1 or j==n-1 :
                print('*',end='')
            else:
                print(' ',end='')
        print('')
def harf_f(n):
    for i in range(n):
        for j in range(n):
            if j == 0 or i == 0 or (i == n//2 and j < n-1):
                print('*', end='')
            else:
                print(' ', end='')
        print()
def harf_g(n):
    for i in range(9):
        for j in range(9):
            if i == 0 or i == n-1 or j == 0 or (i > n//2 and j == n-1) or (i == n//2 and j > n//2) or (i > n//2 and i < n-1 and j == n//2):
                print('*', end='')
            else:
                print(' ', end='')
        print()
def harf_h(n):
    for i in range(n):
        for j in range(n):
            if j == 0 or j == n-1 or i == n//2:
                print('*', end='')
            else:
                print(' ', end='')
        print()
def harf_j(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or (j == n//2 and i < n-1) or (i == n-1 and j < n//2) or (j == 0 and i > n//2):
                print('*', end='')
            else:
                print(' ', end='')
        print()
def harf_k(n):
    for i in range(n):
        for j in range(n):
            if j == 0 or (i + j == n-1) or (i - j == 0 and i >= n//2):
                print('*', end='')
            else:
                print(' ', end='')
        print()
def harf_l(n):
    for i in range(n):
        for j in range(n):
            if j == 0 or i == n-1:
                print('*', end='')
            else:
                print(' ', end='')
        print()
def harf_z(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or (i + j == n-1):
                print('*', end='')
            else:
                print(' ', end='')
        print()
def harf_x(n):
    for i in range(n):
        for j in range(n):
            if (i == j) or (i + j == n-1):
                print('*', end='')
            else:
                print(' ', end='')
        print()
def harf_v(n):
    for i in range(n):
        for j in range(n):
            if i==n//2+1:
                return ''
            elif j == i:
                print('*', end='')
            elif j == n - i - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()
def harf_b(n):
    for i in range(n):
        for j in range(n):
            if (i==0 and j==n-1) or (i==n-1 and j==n-1) or (i==n//2 and j==n-1):
                print(' ',end='')
            elif i==0 or j==n-1 or j==0 or i==n//2 or i==n-1:
                print('*',end='')
            else:
                print(' ',end='')
        print('')
def harf_c(n):
    t=[]
    for i in range(n):
        for j in range(n):
            t.append(j)
            if (i==0 and j==0) or (i==0 and j==n-1) or (i==n-1 and j==0):
                print(' ',end='')
            elif (i==1 and j==n-1) or (i==n-2 and j==n-1) or i==0 or j==0 or (i==n-1 and j!=n-1):
                print('*',end='')
            else:
                print(' ',end='')
        print('')
def harf_n(n):
    for i in range(n):
        for j in range(n):
            if j == 0 or j == n-1 or i == j:
                print('*', end='')
            else:
                print(' ', end='')
        print()
def harf_m(n):
    for i in range(n):
        for j in range(n):
            if j == 0 or j == n-1 or (i == j and i <= n//2) or (i + j == n-1 and i <= n//2):
                print('*', end='')
            else:
                print(' ', end='')
        print()
def harf_w(n):
    for i in range(n):
        for j in range(n):
            if j == 0 or j == n-1 or (i == j and i >= n//2) or (i + j == n-1 and i >= n//2):
                print('*', end='')
            else:
                print(' ', end='')
        print()

a=input('hohlagan gapizni yozing:')
satr=list(a)

d={'q':harf_q,
   'e':harf_e,
   'r':harf_r,
   't':harf_t,
   'y':harf_y,
   'u':harf_u,
   'i':harf_i,
   'o':harf_o,
   'p':harf_p,
   'a':harf_a,
   's':harf_s,
   'd':harf_d,
   'f':harf_f,
   'g':harf_g,
   'h':harf_h,
   'j':harf_j,
   'k':harf_k,
   'l':harf_l,
   'z':harf_z,
   'x':harf_x,
   'c':harf_c,
   'v':harf_v,
   'b':harf_b,
   'n':harf_n,
   'm':harf_m,
   'w':harf_w,
   }
for i in satr:
    if i==' ':
        continue
    g=i.lower()
    d[g](n)
    print()
    print()