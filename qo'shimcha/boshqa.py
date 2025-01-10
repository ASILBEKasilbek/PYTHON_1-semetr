# b=list(map(int,input().split()))
# a=len(b)
# if a%2==1:
#     print(*[0]*(a//2),b[a//2],*[1]*(a//2))
# else:
#     print(*[0]*(a//2),*[1]*(a//2))



# b=list(map(int,input().split()))
# t=[0]*(len(b)//2)+[1]*(len(b)//2)
# if len(b)%2==0:
#     print(*t)
# else:
#     k=b[len(b)//2]
#     t.insert(len(b)//2,k)
#     print(*t)


# b=list(map(int,input().split()))
# t=[]
# if len(b)%2==1:
#     for i in range(len(b)):
#         if i<len(b)//2:
#             t.append(0)
#         elif i>len(b)//2:
#             t.append(1)
#         else:
#             t.append(b[len(b)//2])
# else:
#     t=[0]*(len(b)//2)+[1]*(len(b)//2)
# print(t)

# a=int(input())
# s=0
# for i in range(1,a//2+1):
#     if a%i==0:
#         s+=1
# print("Tub son"*(s==1) or "Tub son emas"*(s!=0))


# n=[i for i in range(1,21)]
# for i in n:
#     if 6<i and i<15:
#         continue
#     print(i)

# def describe_number(x):
#     match x:
#         case 1:
#             return "Bir"
#         case 2:
#             return "Ikki"
#         case _:
#             return "Boshqa raqam"

# print(describe_number(6))
# n=int(input())
# s=0
# for i in range(1,n*n+1):
#     print(i,end=' ')
#     s+=i
#     if i%n==0:
#         print('')
# print(int(s/n))


# n=9
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==n-1 or j==0 or i==n//2:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print('')

# def chiz_a():
#     matritsa = [[' ' for _ in range(9)] for _ in range(9)]
    
#     # 'A' harfi shaklini chizish
#     for i in range(9):
#         matritsa[i][0] = '*'
#         matritsa[i][8] = '*'
    
#     for i in range(9):
#         matritsa[0][i] = '*'
#         matritsa[4][i] = '*'
    
#     # Matritsani chiqarish
#     for qator in matritsa:
#         print(''.join(qator))

# chiz_a()
# n=8
# for i in range(1):
#     k=0
#     for i in range(n):
#         for j in range(n):
#             if i==n//2:
#                 return ''
#             elif j == i:
#                 print('*', end='')
#             elif j == n - i - 1:
#                 print('*', end='')
#             else:
#                 print(' ', end='')
#         print()