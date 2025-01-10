
n=int(input())
k=int(input())
t=0
x=n
w=False
for i in range(1,n+1):
    for j in range(1,k+1):
        if w:
            x+=2
            t-=1
        print(' '*t+'*'*x)
        if w==False:
            t+=1;x-=2
        if x==1:
            w=True
            x+=2
            t-=1
            print('13')
    print(i)

# print('*'*(n+2))
# for i in t:
#     if i==0:
#         print(' '*a+'*')
#         continue
#     print(' '*a+'*'+'*'*i+'*')
#     a+=1
# t.reverse()
# for i in t:
#     if i==0:
#         print(' '*a+'*')
#         a-=1
#         continue
#     print(' '*a+'*'+' '*i+'*')
#     a-=1
# print('*'*(n+2))


    