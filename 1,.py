# n=int(input());k=25
# t=[i for i in range(n*n)]
# print(t[n*n-3*(n-1)])
# s=0
# for i in range(n):
#     for j in range(n):
#         if i==0:
#             print(k,end='')
#             k-=1
#         else:
#             print(' ',end='')
#         if j==n-1:
#             print(k)
#             k-=1
#         else:
#             print(' ',end='')
#         if i==n-1:
#             print(t[n*n-3*(n-1)]+s,end='')
#             s+=1
#         else:
#             print(' ',end='')
#     print()








def add(s,a,b):
    s=list(s)
    if a<0 or b<0:
        return "son manfiykuu"
    elif a>b:
        return "startni finishdan katta kiritildi"
    elif a==b:
        return "tengku"
    else:
        if len(s)<a:
            return "matn uzunligi kichkinakuuu"
        k=''
        if a!=0:
            a-=1
        for i in range(a,b):
            try:
                k+=s[i]
            except:
                continue
        return k
    


s=input()
a=int(input())
b=int(input())
print(add(s,a,b))

