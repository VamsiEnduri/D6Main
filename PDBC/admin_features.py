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

def add_student(a,b,c,d,e,f):
    q="insert into students2 (s_name,s_email,s_phnum,s_t_id,s_b_id,s_a_id) values (%s,%s,%s,%s,%s,%s)"
    curObj.execute(q,(a,b,c,d,e,f))
    conn.commit()
    print("student added successfullyyy.....")

def fetch_all_trainers():
    query="select * from trainers"
    curObj.execute(query)
    data=curObj.fetchall()
    print(data)
    print("fethed all traniers data")

def fetch_all_batches():
    query="select * from batches"
    curObj.execute(query)
    data=curObj.fetchall()
    print(data)
    print("fethed all batches data")
    
def fetch_all_students():
    query="select * from students2"
    curObj.execute(query)
    data=curObj.fetchall()
    print(data)
    print("fethed all students data")    
        
def fetch_t_b_data(id):
    query="""
             select t_id,t_name,t_email,b_id,b_name
             from trainers 
             inner join batches
             on trainers.t_id = batches.trainer_id
             where trainers.t_id =%s
    """
    curObj.execute(query,(id,))
    data=curObj.fetchall()
    print(data)
    print("trainers+batch data fetched successfully........")


def fetch_t_s_data(id):
    query="""
             select t_id,t_name,t_email,s_name,s_email,s_b_id
             from trainers 
             right join students2
             on trainers.t_id = students2.s_t_id
             where trainers.t_id =%s
    """
    curObj.execute(query,(id,))
    data=curObj.fetchall()
    print(data)
    print("trainers+students data fetched successfully........")


