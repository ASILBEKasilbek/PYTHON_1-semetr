

def ha(n):
   if n < 0:
      n = -n
   if n == 0 or n < 10:
      return 1
   else:
      return 1 + ha(n // 10)
n=int(input())
print(ha(n))