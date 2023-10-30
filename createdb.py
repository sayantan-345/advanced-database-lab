import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='Marcosbose1234@')

mycursor=conn.cursor()
mycursor.execute("SHOW DATABASES")
for i in mycursor:
    print(i)

