import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='Marcosbose1234@')

mycursor=conn.cursor()
mycursor.execute("create table dj.Stu(name varchar(100) ,roll_no int(2) ,age int(2) ,marks float);")
conn.close()

