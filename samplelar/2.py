# n=int(input())

# t=[0]*n
# t.insert(0,1)
# t.pop()
# k=1
# p=1
# s=0
# while s<n//2:
#     s+=1
#     p+=(2*n-1) 
#     t.insert(k,p)
#     t.pop()
#     p+=1
#     k+=1
#     t.insert(k,p)
#     t.pop()
#     k+=1
# print(t)


# a="zexrtcyvubivcg"
# s=''
# for i in range(len(a)-1,-1,-1):
#     s+=a[i]
# print(s)


# a=input().split()
# s=[]
# for i in a:
#     k=''
#     for j in range(len(i)-1,-1,-1):
#         k+=i[j]
#     s.append(k)
# print(*s)


# p=0;s=0
# def ha(n,k):
#     global p,s
#     if k==int(str(n)[p]):
#         return s
#     else:
#         s+=int(str(n)[p])
#         p+=1
#         return ha(n,k)
# n=int(input())
# k=int(input())
# print(ha(n,k))



# a=map(int,input().split())
# s=[]
# for i in a:
#     while len(str(i))>1:
#         s.append(i%10)
#         i=i//10
#     s.append(i)
# print(s)



# a=list(map(int,input().split()))
# s=[]
# while len(a)>=2:
#     s.append(a[0]+a[-1])
#     a.pop(-1)
#     a.pop(0)
# print(s)




