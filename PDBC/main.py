# i wanna login as admin
from admin_features import create_trainer,create_batch,add_student,fetch_all_trainers,fetch_all_batches,fetch_all_students,fetch_t_b_data,fetch_t_s_data
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
           4. fetch all trainers
           5. fetch all batches
           6. fetch all students
           7. fetch trainers + their batches data only
           8. fetch trainers + their studnets data only
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
        elif i == 3:
            s_n=input("enter s_name here :--- ")
            s_e=input("enter s_email here :--- ")
            s_ph=input("enter s_phNum  here :--- ")
            s_t_id=int(input("enter s_trainer_id  here :--- "))
            s_b_id=int(input("enter s_batch_id  here :--- "))
            s_a_id=int(input("enter s_admin_id  here :--- "))
            add_student(s_n,s_e,s_ph,s_t_id,s_b_id,s_a_id)
        elif i == 4:
            fetch_all_trainers()
        elif i == 5:
            fetch_all_batches()    

        elif i ==6:
            fetch_all_students()
        elif i ==7 :
            t_id=int(input("enter trainer id to get all his data with his batches data"))    
            fetch_t_b_data(t_id)
        elif i == 8:
            t_id=int(input("enter trainer id to get all his data with his batches data"))    
            fetch_t_s_data(t_id)

else:
    print("not valid admin")

