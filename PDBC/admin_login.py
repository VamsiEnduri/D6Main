from db_c import curObj
def admin_login():
    a_e=input("enter email here :--- ")
    a_p=input("enter password  here :--- ")
    query="select * from admins where admin_id=%s"
    curObj.execute(query,(1,)) # query,()
    data=curObj.fetchone()
    print(data)
    if a_e == data[2] and a_p==data[3]:
        return True
        # print("yes")
    else:
        return False        