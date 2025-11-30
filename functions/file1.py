# # # # # function :-- 

# # # # # function  is block of code which can be reusable multiple time when we wanna use it 

# # # # # def func_name():
# # # # #     #code 
# # # # # func_name()  
# # # name="vamsi"
# # # age=27
# # # def add():
# # #     a=10
# # #     b=20
# # #     c=a+b
# # #     print(c)
# # # add()    
# # # # #login function
from loginFeature import login__
from registerFeature import register__
rUsers=[]


while True:
    print("1. register...")
    print("2. login ....")
    i=int(input("enter yr choice :--   like 1 r 2 :--   "))
    if i == 1:
        newUser=register__()
        rUsers.append(newUser)
    if i == 2:
        login__(rUsers)    

# def login():
#     u_name="vamsi__"
#     password="vamsi@123"
#     u=input("enter name here ;-- ")
#     p=input("enter password here -- ")
#     if u_name == u and password == p:
#         print("loggedin successfully.............")
#     else:
#         print("invalid credentials")    
# login()    

# rUsers=[]

# def register():
#     name=input("enter name here :--- ")
#     age=input("enter age here :--- ")
#     batchNo=input("enter batchNo here :--- ")
#     passedoutYear=input("enter passedoutYear here :--- ")
#     stream=input("enter stream here :--- ")
#     passsword=input("password here :--  ")
#     cPasssword=input("confirm password here :--  ")
#     if cPasssword==passsword:
#         newUser={
#             "n":name,
#             "a":age,
#             "bNo":batchNo,
#             "pYear":passedoutYear,
#             "s":stream,
#             "p":passsword
#         }
#         rUsers.append(newUser)

# register() 
# # # # print(rUsers)   


# # # how many type of functions are there  in python ?
# # # 2 types functions

# # # inbuilt :-- input(),print(),sum(),min(),max() etc...
# # # userdefined :-- login().add(),register()


# # # function with args and params
# # # args vs params
# # # u=input("enter uname :-- ")
# # # p=input("enter password :-- ")
# # # def login(x,y,l): #parameters params
# # #     print(x)
# # #     print(y)
# # #     print(l)
# # # login(u,p,"hyd") #calling r invoking   #arguments args u, p  


# # # function with default params 

# # # def details(name="vamsi",age=27):
# # #     print(name,age)
# # # details()    


# # # function with default params and args


# # # def details(y,name="vamsi",age=27):
# # #     print(y,name,age)
# # # details(456,1234,12345)    



# # # function with return 

# prevSal=50000
# def salaryInce(pSal):
#     thirdPercFromMySal=pSal*1.3 # 50000 * 1.3= 100000
#     print(thirdPercFromMySal)
# salaryInce(prevSal)

# # prevSal=50000
# # def salaryInce(pSal):
# #     thirdPercFromMySal=pSal*0.3
# #     totalSalaryAfterInc=pSal+thirdPercFromMySal
# #     print(totalSalaryAfterInc)

# # salaryInce(prevSal)
