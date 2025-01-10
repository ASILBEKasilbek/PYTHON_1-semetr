# n=int(input())
# s=n
# k=0 if n%2==0 else 1
# while n!=0:
#     s+=n//2+k
#     n//=2
#     k=0
# print(s)



# n=int(input())
# a=[0]*n
# s=n
# while len(a)>1:
#     s+=len(a)//2
#     for i in range(len(a)//2):
#         a.remove(0)
# print(s)


# k=65
# while k<90:
#     print(chr(k),end=' ')
#     k+=1
#     if k%5==0:
#         print()


# n=int(input())
# i=1
# while i<n+1:
#     print(i,n-i+1)
#     i+=1
n=int(input());i=0
while i<n: 
    print('Salom' if i%2==0 else 'Hayr');i+=1