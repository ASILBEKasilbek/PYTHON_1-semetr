import string
a = string.ascii_lowercase
k=0
while True:
    print("\033[32m Bu matn yashil rangda.\033[0m",end=' ')
    print("\033[31m Bu matn qizil rangda.\033[0m",end=' ')
    print("\033[33mBu matn sariq rangda.\033[0m",end=' ')
    print("\033[35mBu matn siyoh rangda.\033[0m",end=' ')
    print(' '*k)
    k+=1
    