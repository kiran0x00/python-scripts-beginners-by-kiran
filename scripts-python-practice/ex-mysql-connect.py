import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="kiran")
cursor=mydb.cursor()
cursor.execute("select * from emp")
cursor.fetchone()
#cursor.fetchall()
for i in cursor:
    print(i)