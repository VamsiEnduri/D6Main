import mysql.connector


db_c=mysql.connector.connect(
    host="localhost",
    user="root",
    database="vamsi1310",
    password="10000Coders"
)

print(db_c,"connection")