def asilbek(n):
    a = [[0] * n for ha in range(n)]
    num = n * n
    l=0;r=n-1;t=0;b=n-1
    while l <= r and t <= b:
        for i in range(l, r + 1):
            a[t][i] = num
            num -= 1
        t += 1
        for i in range(t, b + 1):
            a[i][r] = num
            num -= 1
        r -= 1
        for i in range(r, l - 1, -1):
            a[b][i] = num
            num -= 1
        b -= 1
        for i in range(b, t - 1, -1):
            a[i][l] = num
            num -= 1
        l += 1
    return a
n = int(input())
q=asilbek(n)
for i in q:
    print(" ".join(str(x).rjust(2," ") for x in i))

