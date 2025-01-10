
for i in range(22):
    for j in range(30):
        if i<=5:
            print("\033[34m#\033[0m",end='')
        elif 6<=i<=7:
            print("\033[31m#\033[0m",end='')
        elif 8<=i<=13:
            print('#',end='')
        elif 14<=i<=15:
            print("\033[31m*\033[0m",end='')
        else:
            print("\033[32m#\033[0m",end='')
    print()
