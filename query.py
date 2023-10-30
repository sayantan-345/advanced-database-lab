import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='Marcosbose1234@')

mycursor=conn.cursor()
mycursor.execute("select * from dj.stu;")
for i in mycursor.fetchall():
    print(i)
conn.close()