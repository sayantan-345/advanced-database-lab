
'''mycursor.execute('insert sayantan.student values(2,"Jane Smith","jane.smith@example.com","987-654-3210","456 Elm St");')
mycursor.execute('insert sayantan.student values(3,"Robert Johnson","robert.j@example.com","555-123-4567","789 Oak Ave");')
mycursor.execute('insert sayantan.student values(4,"Emily White","emily.white@example.com","111-222-3333","567 Pine St");')
mycursor.execute('insert sayantan.student values(5,"Michael Lee","michael.lee@example.com","333-444-5555","789 Cedar Dr");')
mycursor.execute('insert sayantan.student values(6,"Sarah Brown","sarah.brown@example.com","555-666-7777","890 Willow Ln");')
mycursor.execute('insert sayantan.student values(7,"David Clark","david.clark@example.com","777-888-9999","123 Birch Ave");')
mycursor.execute('insert sayantan.student values(8,"Melissa Turner","melissa.turner@example.com","888-999-0000","456 Redwood Rd");')'''
'''values = [('course_id{}'.format(i), 'coursename{}'.format(i),'credits{}'.format(i)) for i in range(0,8)]
c = conn.cursor()
c.executemany("INSERT INTO sayantan.course(course_id, coursename,credits) VALUES(?,?)", values)'''
'''import mysql.connector
from datetime import datetime
def insert_varibles_into_table(examid, examdate, examtime,examlocation):
    try:
        connection = mysql.connector.connect(host='localhost',user='root',password='Marcosbose1234@')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO sayantan.exam (examid, examdate,examtime,examlocation) 
                                VALUES (%s, %s, %s,%s) """

        record = (examid, examdate, examtime,examlocation)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into course table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

for i in range(0,8):
    examid=int(input("enter the number"))
    examdate=(input("enter exam date"))
    examtime=(input("enter the examtime"))
    #parsetime=datetime.strptime(examtime, "%I:%M %p")
    #formattedtime = parsetime.strftime("%H:%M:%S")
    examlocation=(input("enter the exam location"))
    insert_varibles_into_table(examid, examdate, examtime, examlocation)'''
'''import mysql.connector
from datetime import datetime
def insert_varibles_into_table( facultyid,name,email,phone,department):
    try:
        connection = mysql.connector.connect(host='localhost',user='root',password='Marcosbose1234@')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO sayantan.faculty ( facultyid,name,email,phone,department) 
                                VALUES (%s, %s, %s,%s,%s) """

        record = ( facultyid,name,email,phone,department)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into faculty table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

for i in range(0,8):
    facultyid=int(input("enter the number"))
    name=(input("enter name"))
    email=(input("enter the email"))
    #parsetime=datetime.strptime(examtime, "%I:%M %p")
    #formattedtime = parsetime.strftime("%H:%M:%S")
    phone=(input("enter the phone number"))
    department=(input("enter the department"))
    insert_varibles_into_table(facultyid,name,email,phone,department)'''
'''import mysql.connector
from datetime import datetime
def insert_varibles_into_table( enrollmentid,studentid,courseid,enrollmentdate):
    try:
        connection = mysql.connector.connect(host='localhost',user='root',password='Marcosbose1234@')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO sayantan.enrollment ( enrollmentid,student_id,course_id,enrollmentdate) 
                                VALUES (%s, %s, %s,%s) """

        record = (enrollmentid,studentid,courseid,enrollmentdate)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into faculty table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

for i in range(0,10):
    enrollmentid=int(input("enter the number"))
    studentid=int(input("enter name"))
    courseid=int(input("enter the email"))
    #parsetime=datetime.strptime(examtime, "%I:%M %p")
    #formattedtime = parsetime.strftime("%H:%M:%S")
    enrollmentdate=(input("enter the phone number"))
    insert_varibles_into_table(enrollmentid,studentid,courseid,enrollmentdate)'''
'''import mysql.connector
from datetime import datetime
def insert_varibles_into_table(teachingid,facultyid,course_id):
    try:
        connection = mysql.connector.connect(host='localhost',user='root',password='Marcosbose1234@')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO sayantan.teaching ( teachingid,facultyid,course_id) 
                                VALUES (%s, %s, %s) """

        record = (teachingid,facultyid,course_id)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into faculty table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

for i in range(0,10):
    teachingid=int(input("enter the number"))
    facultyid=int(input("enter name"))
    course_id=int(input("enter the email"))
    #parsetime=datetime.strptime(examtime, "%I:%M %p")
    #formattedtime = parsetime.strftime("%H:%M:%S")
    #enrollmentdate=(input("enter the phone number"))
    insert_varibles_into_table(teachingid,facultyid,course_id)'''
'''import mysql.connector
from datetime import datetime
def insert_varibles_into_table( registrationid,student_id,examid,registrationdate):
    try:
        connection = mysql.connector.connect(host='localhost',user='root',password='Marcosbose1234@')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO sayantan.examregistration ( registrationid,student_id,examid,registrationdate) 
                                VALUES (%s, %s, %s,%s) """

        record = (registrationid,student_id,examid,registrationdate)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into faculty table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

for i in range(0,10):
    registrationid=int(input("enter the number"))
    student_id=int(input("enter name"))
    examid=int(input("enter the email"))
    #parsetime=datetime.strptime(examtime, "%I:%M %p")
    #formattedtime = parsetime.strftime("%H:%M:%S")
    registrationdate=(input("enter the phone number"))
    insert_varibles_into_table(registrationid,student_id,examid,registrationdate)'''
'''import mysql.connector
from datetime import datetime
def insert_varibles_into_table( resultid,student_id,examid,score):
    try:
        connection = mysql.connector.connect(host='localhost',user='root',password='Marcosbose1234@')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO sayantan.examresult ( resultid,student_id,examid,score) 
                                VALUES (%s, %s, %s,%s) """

        record = (resultid,student_id,examid,score)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into faculty table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

for i in range(0,10):
    resultid=int(input("enter the number"))
    student_id=int(input("enter name"))
    examid=int(input("enter the email"))
    #parsetime=datetime.strptime(examtime, "%I:%M %p")
    #formattedtime = parsetime.strftime("%H:%M:%S")
    score=(input("enter the phone number"))
    insert_varibles_into_table(resultid,student_id,examid,score)'''