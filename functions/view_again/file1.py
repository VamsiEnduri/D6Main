from login import login 
from register import register
rUsers=[]
while True:
    print("1. register...")
    print("2. login ....")
    i=int(input("enter yr choice :--   like 1 r 2 :--   "))
    if i == 1:
        newUser=register()
        rUsers.append(newUser)
    if i == 2:
        login(rUsers)  