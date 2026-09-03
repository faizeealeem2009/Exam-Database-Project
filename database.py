import mysql.connector
try:
    conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="bismillah",
    database="Exam"
    )
except:
    print("Unable to connect the database")
else:
    print("Connection Established")
    mycursor=conn.cursor()
    #mycursor.execute("DROP TABLE students;")
    mycursor.execute("SHOW TABLES")
    for c in mycursor.fetchall():
        print(c)