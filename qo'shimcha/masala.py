#1
s=0
for i in range(101):
    s+=i    
print(s)




#2
juft=0
toq=0
for i in range(51):
    if i%2==0:
        juft+=i
    else:
        toq+=i
print("Toq=",toq,"Juft=",juft)

#3
s=0
for i in range(-77,81,7):
    s+=1
print(s)



#4
s=0
l=input().split()
for i in l:
    if i=="Olma" or i=="olma":
        s+=1
print(s)


#5
juft=0
toq=0
a=int(input())
b=int(input())
for i in range(a,b+1):
    if i%2==0:
        juft+=i
    else:
        toq+=i
print("Toq=",toq,"Juft=",juft)


#6
s=0
l=list(map(int,input().split()))
for i in l:
    if i%2==0:
        s+=1
print(s)



#7
s=0
a=input()
for i in range(len(a)):
    if a[i]==a[i].upper():
        s+=1
print(s)



#8
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)



#9

l=list(map(int,input().split()))
print(*[i*2.54 for i in l])



#10

l=list(map(int,input().split()))
print(*[i for i in l if i>10 and i%2==0])




#11

l=list(map(int,input().split()))
print(*[i%3 for i in l])




#12

l=input().split()
print(*[i for i in l if i[0]=="o"])




