from db_c import curObj,conn
def create_trainer(n,e,ph,a_id):
    q="insert into trainers (t_name,t_email,t_ph,admin_id) values (%s,%s,%s,%s)"
    curObj.execute(q,(n,e,ph,a_id))
    conn.commit()
    print("trainer add successfullyyy.....")

def create_batch(a,b,c):
    q="insert into batches (b_name,admin_id,trainer_id) values (%s,%s,%s)"
    curObj.execute(q,(a,b,c))
    conn.commit()
    print("batch added successfullyyy.....")

