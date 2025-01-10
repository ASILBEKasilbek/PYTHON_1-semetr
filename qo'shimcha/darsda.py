# a=['Dushanba','Seshanba','Chorshanba','Payshanba','Juma','Shanba','Yakshanba']
# for i in range(4):
#     print(f'{i+1} hafta')
#     for j in a:
#         print('\t',j)



# qator=int(input())
# ustun=int(input())
# for i in range(qator):
#     print('0',end=' ')
#     for j in range(ustun-1):
#         print('*',end=' ')
#     print()


# a = list(map(int,input().split()))
# for i in range(len(a)):
#     for j in range(0, len(a)-i-1):
#         if a[j]>a[j+1]:
#             k=a[j]
#             a[j]=a[j+1]
#             a[j+1]=k
# print(a)



# a = list(map(int,input().split()))
# for i in range(len(a)):
#     for j in range(0, len(a)-i-1):
#         if a[j]>a[j+1]:
#             k=a[j]
#             a[j]=a[j+1]
#             a[j+1]=k
# print(a)




# a=list(map(int,input().split()))
# n=len(a)
# i=0
# while i<n:
#     j=0
#     while j<n-i-1:
#         if a[j]>a[j+1]:
#             k=a[j]
#             a[j]=a[j+1]
#             a[j+1]=k
#         j+=1
#     i+=1
# print(a)




# a = list(map(int, input().split()))
# n = len(a)

# for i in a:
#     s = False
#     for j in a:
#         if a[j] > a[j + 1]:
#             k=a[j]
#             a[j]=a[j+1]
#             a[j+1]=k
#             s = True
#     if not s:
#         break

# print(a)


# a = list(map(int, input().split()))
# n = len(a)
# i = 0
# for q in a:
#     s = False
#     j = 0
#     for q1 in a:
#         if j < n - 1:
#             if a[j] > a[j + 1]:
#                 k=a[j]
#                 a[j]=a[j+1]
#                 a[j+1]=k
#                 s = True
#             j += 1
#     if not s:
#         break
#     i += 1
# print(a)






