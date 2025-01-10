def Digitilcount(n):
    return len(str(n)),sum(map(int,list(str(n))))


n=int(input())
print(Digitilcount(n))