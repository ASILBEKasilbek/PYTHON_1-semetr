def uzunlik(n):
    s=0
    k=''
    while n!=k:
        k+=n[s]
        s+=1
    return s
def past(n):
    d4={
    'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g',
    'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n',
    'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u',
    'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z',
    'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g',
    'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n',
    'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u',
    'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z','1':'1','2':'2','3':'3',
    '4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','0':'0',
    '!':'!','@':'@','#':'#','%':'%','$':'$','^':'^','&':'&','*':'*','(':'(',
    '-':'-','_':'_','+':'+','=':'=','{':'{','[':'[',']':']','|':'|',')':')',
    '>':'>','<':'<',',':',','.':'.','~':'~','`':'`','}':'}','?':'?','/':'/',' ':' ',
    "'":"'",'"':'"',";":";",":":":"
    }
    s=''
    for i in range(uzunlik(n)):
        s+=d4[n[i]]
    return s
a=input()
d3='abcdefghijklmnopqrstuvwxyz'
d4='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
d5='1234567890'
q=0
for i in range(uzunlik(a)):
    for j in d3:
        if j==a[i]:
            q=1
            continue
    if q:
        continue
r=0
for i in range(uzunlik(a)):
    for j in d4:
        if j==a[i]:
            r=1
            continue
    if r:
        continue
y=0
for i in range(uzunlik(a)):
    for j in d5:
        if j==a[i]:
            y=1
            continue
    if y:
        continue
t=1
if r and q and y and uzunlik(a)>8:
    for i in range(uzunlik(a)-2):
        if past(a[i])==past(a[i+1]) or past(a[i])==past(a[i+2]) or past(a[i+1])==past(a[i+2]):
            t=0
    if t:
        print('Yaroqli')
    else:
        print('Yaroqsiz')
else:
    print('Yaroqsiz')