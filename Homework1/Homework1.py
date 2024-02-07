import mysql.connector
from mysql.connector import Error
def create_connection (hostname, uid, pwd, dbname):
    conn = None
    try:
        conn = mysql.connector.connect(
            host = hostname,
            user = uid,
            password = pwd,
            database = dbname
        )
        print("DB created successfully")
    except Error as e:
        print("Error is", e)
    return conn

myconn = create_connection('sp2024db.c7ugmewi8xhh.us-east-1.rds.amazonaws.com', 'admin', 'Gau113114115116!', 'sp2024db')
mycursor = myconn.cursor(dictionary=True)
mycursor.execute('select* from users')
userlist = mycursor.fetchall()
print(userlist)