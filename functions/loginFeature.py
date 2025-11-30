# from file1 import rUsers 
def login__(allUsers):
    u=input("enter name here ;-- ")
    p=input("enter password here -- ")
    for i in allUsers:
        if i["n"] == u and i["p"]  ==p:
            print("login successful")
            break
        else:
            print("invalid")    
            continue
