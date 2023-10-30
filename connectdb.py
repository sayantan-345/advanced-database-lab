import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='Marcosbose1234@')
if conn.is_connected():
    print("connection successful")
    