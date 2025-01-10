n = int(input())
s = 0
b = 1
for i in range(1, n + 1):
    b *= i 
    s += 1/b  
print(s)
