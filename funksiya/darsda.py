# def sanoq(a,n):
#     s=0
#     for i in range(len(a)):
#         if a[i]==n:
#             s+=1
#     return s
# a=input()
# n=input()
# print(sanoq(a,n))

# def matn(a):
#     k=[]
#     s=''
#     for i in range(len(a)-1):
#         if a[i]==' ' and a[i+1]==' ':
#             continue
#         elif a[i]==' ':
#             k.append(s)
#             s=''
#         else:
#             s+=a[i]
#     s=''
#     for i in range(1,len(a)):
#         print(a)
#         print(a[-i])
#         if a[-i]==' ':
#             k.append(s)
#             break
#         else:
#             s+=a[i]
#     return k 
# a=input()
# print(matn(a))

# def uzunlik(n):
#     s=0
#     k=''
#     while n!=k:
#         k+=n[s]
#         s+=1
# #     return s

# a=list(map(int,input().split()))
# def d(a):
#     k=[]
#     for i in a:
#         t=0
#         if i<0:
#             i=-1*i
#         while i!=0:
#             t+=i%10
#             i//=10
#         k.append(t)
#     return k
# print(*d(a))



# def dectobinary(n,k):
#     s=''
#     while n>0:
#         d=n%k
#         s+=str(d)
#         n=n//k
#     s=list(s)
#     s.reverse()
#     k=''
#     for i in s:
#         k+=i
#     return k
# a=int(input())
# k=int(input())
# print(dectobinary(a,k))
# print(bin(a))

n=int(input())
a=100
def jon(a):
    k=1;k1=1;d=[]
    while a>0:
        a-=k
        d.append(k)
        k=k+k1
        k1=sum(d)
    return d
k=jon(a)
print(k)
for i in range(len(k)):
    if k[i]==n:
        continue
    print(i+1,'-chisi',a-k[i])