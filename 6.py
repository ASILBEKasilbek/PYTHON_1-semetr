import random as r
k=r.randint(1,100)
n=int(input("man bitta son o'yladim siz son kiriting:"))
while n!=k:
    if n<k:
        print("man o'ylagan son bu sondan katta")
    else:
        print("man o'ylagan son bu sondan kichik")
    n=int(input('son kiriting:'))
print("To'g'ri siz g'alaba qozondiz")
