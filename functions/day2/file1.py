# # varaible length args *args
# def empDetails(*a):
#     print(a)
# empDetails("vamsi,27","10000coders",88000)    


# #key args functions
# def abc(name22,age):
#     print(name22,age)
# abc(name22="vamsi",age=27) #key:value :-- args    

# # key word varible length args
# def abc(**b):
#     print(b)
# abc(name22="vamsi",age=27)
# scope :-- 
# scope is specoific place where i can access  specoific var r specoific functions

company ="10000coders" # global var
print(company)
def empDetails():
    name="vamsi"# function empdetails var r local vara
    print(name)
    print(f"{name} is wprking in {company}")
empDetails() 
print(company)  
