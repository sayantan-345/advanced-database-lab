#import mysql.connector
#conn=mysql.connector.connect(host='localhost',user='root',password='Marcosbose1234@')

#mycursor=conn.cursor()
'''for i in range(0,8):
    print("enter data for row",i+1)
    course_id=int(input("enter the number:-"))
    coursename=(input("enter the name:-"))
    credits=int(input("enter the number:-"))
    mycursor.execute("insert into sayantan.course(course_id,coursename,credits),'values(%d,%s,%d)';")'''
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
import mysql.connector

def insert_varibles_into_table(course_id, coursename, credits):
    try:
        connection = mysql.connector.connect(host='localhost',user='root',password='Marcosbose1234@')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO Laptop (course_id, coursename, credits) 
                                VALUES (%s, %s, %s, %s) """

        record = (course_id, coursename, credits)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into Laptop table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


#insert_varibles_into_table(101, 'Mathematics', 6999, '2019-04-14')
#insert_varibles_into_table(3, 'MacBook Pro', 2499, '2019-06-20')
#conn.commit()
#conn.close()
for i in range(0,8):
    course_id=int(input("enter the number"))
    coursename=(input("enter coursename"))
    credits=int(input("enter the credit"))