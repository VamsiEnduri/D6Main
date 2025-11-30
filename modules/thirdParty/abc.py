import mysql.connector


db_c=mysql.connector.connect(
    host="localhost",
    user="root2",
    database="d6_main",
    password="10000Coders"
)

print(db_c,"connection")