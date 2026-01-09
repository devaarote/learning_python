import mysql.connector

myconn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="testdb"
    )

mycur=myconn.cursor()

mycur.execute("show tables")

for i in mycur:
    print(i)


myconn.close()