# i wanna login as admin
from admin_features import create_trainer,create_batch
from admin_login import admin_login
admin_login_status=admin_login()
print(admin_login_status,"5 main.py")

if admin_login_status:
    print("super admin login successfulyyyyyyyyyyyy.............")
    while True:
        print("""
           1. create trainer
           2.create batches
           3.create students
           4.exit
        """)
        i=int(input("enetr yr choice here :--  "))
        if i== 1:
            t_n=input("enter t_name here :--- ")
            t_e=input("enter t_email here :--- ")
            t_ph=input("enter t_phnum  here :--- ")
            ad_id=int(input("enter ad_id  here :--- "))
            create_trainer(t_n,t_e,t_ph,ad_id)
        elif i== 2:
            b_n=input("enter b_name here :--- ")
            t_id=int(input("enter t_id here :--- "))
            ad_id=int(input("enter ad_id  here :--- "))
            create_batch(b_n,ad_id,t_id)    
else:
    print("not valid admin")

